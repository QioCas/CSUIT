import streamlit as st
import polars as pl
from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile
import os
import math

st.set_page_config(page_title="Category Relationship Graph", layout="wide")

# ── Data Loading ──────────────────────────────────────────────
@st.cache_data
def load_data():
    items = pl.read_parquet('./items.parquet')
    trans = pl.read_parquet('./transactions-202411-to-202412.parquet')
    return items, trans


@st.cache_data
def build_score(use_l2: bool, use_lift: bool, _items: pl.DataFrame, _trans: pl.DataFrame):
    """Return a scored DataFrame with columns [A, B, score, co_count, lift, p_B_given_A, p_A_given_B]."""
    if not use_l2:
        df = (
            _trans
            .join(
                _items.select(['item_id', 'category_l1']),
                on='item_id',
                how='left'
            )
            .filter(pl.col('category_l1').is_not_null())
        )
        baskets = (
            df
            .group_by(['customer_id', 'updated_date', 'location'])
            .agg(pl.col('category_l1').unique().alias('cats'))
        )
    else:
        df = (
            _trans
            .join(
                _items.select(['item_id', 'category_l1', 'category_l2']),
                on='item_id',
                how='left'
            )
            .filter(
                pl.col('category_l1').is_not_null(),
                pl.col('category_l2').is_not_null()
            )
        )
        baskets = (
            df
            .group_by(['customer_id', 'updated_date', 'location'])
            .agg(
                (pl.col('category_l1') + ' + ' + pl.col('category_l2'))
                .unique().alias('cats')
            )
        )

    counts = (
        baskets
        .explode('cats')
        .group_by('cats')
        .agg(pl.len().alias('count_A'))
        .rename({'cats': 'A'})
    )

    pairs = (
        baskets
        .explode('cats')
        .rename({'cats': 'A'})
        .join(
            baskets
            .explode('cats')
            .rename({'cats': 'B'}),
            on=['customer_id', 'updated_date', 'location'],
            how='inner'
        )
        .filter(pl.col('A') < pl.col('B'))
        .group_by(['A', 'B'])
        .agg(pl.len().alias('co_count'))
    )

    N = baskets.select(pl.len().alias('N')).item()

    result = (
        pairs
        .join(counts, on='A', how='left')
        .join(
            counts.rename({'A': 'B', 'count_A': 'count_B'}),
            on='B',
            how='left'
        )
        .with_columns([
            (pl.col('co_count') / pl.col('count_A')).alias('p_B_given_A'),
            (pl.col('co_count') / pl.col('count_B')).alias('p_A_given_B'),
            (
                pl.col('co_count') * N /
                (pl.col('count_A') * pl.col('count_B'))
            ).alias('lift')
        ])
    )

    if use_lift:
        result = (
            result
            .with_columns([
                (
                    pl.when(pl.col('lift') > 1)
                    .then(pl.col('co_count').log() * pl.col('lift').log())
                    .otherwise(0.0)
                ).alias('score')
            ])
        )
    else:
        result = (
            result
            .with_columns([
                (
                    pl.col('co_count').log() *
                    (pl.col('p_B_given_A') + pl.col('p_A_given_B'))
                ).alias('score')
            ])
        )

    result = (
        result
        .filter(pl.col('score') > 0)
        .sort('score', descending=True)
    )

    return result


# ── Graph Builder ─────────────────────────────────────────────
PALETTES = [
    "#e6194b", "#3cb44b", "#4363d8", "#f58231", "#911eb4",
    "#42d4f4", "#f032e6", "#bfef45", "#fabed4", "#469990",
    "#dcbeff", "#9A6324", "#fffac8", "#800000", "#aaffc3",
    "#808000", "#ffd8b1", "#000075", "#a9a9a9", "#e6beff",
]


def build_pyvis_graph(
    scores: pl.DataFrame,
    height: str = "700px",
    top_n: int = 200,
    min_score: float = 0.0,
    highlight_same_l1: bool = False,
):
    df = (
        scores
        .filter(pl.col('score') >= min_score)
        .head(top_n)
    )

    if df.height == 0:
        return None

    net = Network(
        height=height,
        width="100%",
        bgcolor="#262730",
        font_color="#fafafa",
        directed=False,
        notebook=False,
    )

    net.barnes_hut(
        gravity=-3000,
        central_gravity=0.15,
        spring_length=50,
        spring_strength=0.002,
        damping=0.12,
    )

    NODE_COLOR = "#f0c27f"  # warm starlight gold

    # Collect unique nodes
    nodes = set(df["A"].to_list()) | set(df["B"].to_list())

    # Node sizes proportional to how often they appear
    node_freq: dict[str, int] = {}
    for col in ["A", "B"]:
        for v in df[col].to_list():
            node_freq[v] = node_freq.get(v, 0) + 1

    max_freq = max(node_freq.values(), default=1)

    # for node in nodes:
    #     size = 5 + 35 * (node_freq.get(node, 1) / max_freq)
    #     net.add_node(
    #         node,
    #         label=node,
    #         color=NODE_COLOR,
    #         size=size,
    #         title=f"{node}\nappears in {node_freq.get(node, 0)} top pairs",
    #         font={"size": 14, "color": "#e0e6ff"},
    #     )
    for node in nodes:
        size = 5 + 35 * (node_freq.get(node, 1) / max_freq)

        node_color_cfg = {
            "background": NODE_COLOR,
            "border": NODE_COLOR,
            "highlight": {
                "background": NODE_COLOR,
                "border": NODE_COLOR,
            },
            "hover": {
                "background": NODE_COLOR,
                "border": NODE_COLOR,
            },
        }

        net.add_node(
            node,
            label=node,
            color=node_color_cfg,
            size=size,
            title=f"{node}\nappears in {node_freq.get(node, 0)} top pairs",
            font={"size": 14, "color": "#e0e6ff"},
            chosen=False,
            borderWidth=0,
            borderWidthSelected=0,
        )
    # Edges
    score_vals = df["score"].to_list()
    max_score = max(score_vals, default=1)

    EDGE_SAME_L1 = "#ff6b6b"   # warm coral for intra-L1 edges
    EDGE_CROSS_L1 = "#4fc3f7"   # constellation blue for cross-L1 edges

    # for row in df.iter_rows(named=True):
    #     width = 1 + 0.9 * (row["score"] / max_score)
    #     if highlight_same_l1:
    #         l1_a = row["A"].split(" + ")[0]
    #         l1_b = row["B"].split(" + ")[0]
    #         edge_color = EDGE_SAME_L1 if l1_a == l1_b else EDGE_CROSS_L1
    #     else:
    #         edge_color = EDGE_CROSS_L1
    #     net.add_edge(
    #         row["A"],
    #         row["B"],
    #         value=width,
    #         title=(
    #             f"score: {row['score']:.4f}\n"
    #             f"co_count: {row['co_count']}\n"
    #             f"lift: {row['lift']:.4f}\n"
    #             f"P(B|A): {row['p_B_given_A']:.4f}\n"
    #             f"P(A|B): {row['p_A_given_B']:.4f}"
    #         ),
    #         color={"color": edge_color, "opacity": 0.45},
    #     )

    for row in df.iter_rows(named=True):
        width = 1 + 0.9 * (row["score"] / max_score)
        if highlight_same_l1:
            l1_a = row["A"].split(" + ")[0]
            l1_b = row["B"].split(" + ")[0]
            edge_color = EDGE_SAME_L1 if l1_a == l1_b else EDGE_CROSS_L1
        else:
            edge_color = EDGE_CROSS_L1

        edge_color_cfg = {
            "color": edge_color,
            "highlight": edge_color,
            "hover": edge_color,
            "opacity": 0.45,
            "inherit": False,
        }

        net.add_edge(
            row["A"],
            row["B"],
            value=width,
            title=(
                f"score: {row['score']:.4f}\n"
                f"co_count: {row['co_count']}\n"
                f"lift: {row['lift']:.4f}\n"
                f"P(B|A): {row['p_B_given_A']:.4f}\n"
                f"P(A|B): {row['p_A_given_B']:.4f}"
            ),
            color=edge_color_cfg,
            chosen=False,
            selectionWidth=0,
        )
    return net

def render_graph(net: Network | None, key: str):
    if net is None:
        st.warning("No pairs found with the current filters.")
        return

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False, dir="/tmp"
    ) as f:
        net.save_graph(f.name)
        f.seek(0)
        html = open(f.name, "r", encoding="utf-8").read()
        os.unlink(f.name)

    custom_js = """
    <script type="text/javascript">
    (function () {
        function hexToRgba(hex, alpha) {
            if (!hex) return "rgba(200,200,200," + alpha + ")";
            hex = hex.replace("#", "");
            if (hex.length === 3) {
                hex = hex.split("").map(c => c + c).join("");
            }
            const r = parseInt(hex.substring(0, 2), 16);
            const g = parseInt(hex.substring(2, 4), 16);
            const b = parseInt(hex.substring(4, 6), 16);
            return `rgba(${r}, ${g}, ${b}, ${alpha})`;
        }

        function initCustomHighlight() {
            if (
                typeof network === "undefined" ||
                typeof nodes === "undefined" ||
                typeof edges === "undefined"
            ) {
                setTimeout(initCustomHighlight, 200);
                return;
            }

            const allNodeIds = nodes.getIds();
            const allEdgeIds = edges.getIds();

            const originalNodes = {};
            const originalEdges = {};
            
            network.setOptions({
                interaction: {
                    selectConnectedEdges: false
                },
                nodes: {
                    chosen: false,
                    borderWidthSelected: 0
                },
                edges: {
                    chosen: false,
                    selectionWidth: 0
                }
            });

            allNodeIds.forEach(function(id) {
                originalNodes[id] = nodes.get(id);
            });

            allEdgeIds.forEach(function(id) {
                originalEdges[id] = edges.get(id);
            });

            function resetGraph() {
                nodes.update(allNodeIds.map(id => originalNodes[id]));
                edges.update(allEdgeIds.map(id => originalEdges[id]));
            }

            function fadeToSelection(selectedNodeId) {
                const connectedNodeIds = network.getConnectedNodes(selectedNodeId);
                const connectedEdgeIds = network.getConnectedEdges(selectedNodeId);

                const keepNodes = new Set([selectedNodeId, ...connectedNodeIds]);
                const keepEdges = new Set(connectedEdgeIds);

                const steps = 10;
                let step = 0;

                const timer = setInterval(function() {
                    step += 1;
                    const t = step / steps;

                    const nodeUpdates = [];
                    const edgeUpdates = [];

                    allNodeIds.forEach(function(id) {
                        const orig = originalNodes[id];
                        const isKeep = keepNodes.has(id);

                        if (isKeep) {
                            nodeUpdates.push({
                                ...orig,
                                id: id,
                                hidden: false
                            });
                        } else {
                            nodeUpdates.push({
                                ...orig,
                                id: id,
                                color: {
                                    background: hexToRgba("#666666", 1 - 0.75 * t),
                                    border: hexToRgba("#666666", 1 - 0.75 * t)
                                },
                                font: {
                                    ...(orig.font || {}),
                                    color: hexToRgba("#aaaaaa", 1 - 0.65 * t)
                                },
                                hidden: false
                            });
                        }
                    });

                    allEdgeIds.forEach(function(id) {
                        const orig = originalEdges[id];
                        const isKeep = keepEdges.has(id);

                        if (isKeep) {
                            edgeUpdates.push({
                                ...orig,
                                id: id
                            });
                        } else {
                            edgeUpdates.push({
                                ...orig,
                                id: id,
                                color: {
                                    ...(orig.color || {}),
                                    color: hexToRgba("#666666", 0.35 - 0.25 * t),
                                    highlight: hexToRgba("#666666", 0.35 - 0.25 * t),
                                    hover: hexToRgba("#666666", 0.35 - 0.25 * t),
                                    opacity: 0.08
                                }
                            });
                        }
                    });

                    nodes.update(nodeUpdates);
                    edges.update(edgeUpdates);

                    if (step >= steps) {
                        clearInterval(timer);
                    }
                }, 25);
            }

            network.off("click");
            network.off("doubleClick");

            network.on("click", function(params) {
                if (params.nodes.length > 0) {
                    resetGraph();
                    fadeToSelection(params.nodes[0]);
                } else {
                    resetGraph();
                }
            });

            network.on("doubleClick", function(params) {
                if (params.nodes.length === 0) {
                    resetGraph();
                }
            });
        }
            
        initCustomHighlight();
    })();
    </script>
    """

    html = html.replace("</body>", custom_js + "</body>")
    components.html(html, height=720, scrolling=False)

# ── Streamlit UI ──────────────────────────────────────────────
items, trans = load_data()

st.title("Category Co-occurrence Graph")
st.caption("Interactive network showing how product categories appear together in baskets.")

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Settings")
    use_lift = st.toggle("Use lift in score", value=True)
    top_n = st.slider("Top N pairs to show", 10, 500, 100, step=10)
    min_score = st.number_input("Minimum score", min_value=0.0, value=0.0, step=0.1, format="%.2f")

# ── Section 1: L1 categories ─────────────────────────────────
st.header("Big Categories (L1)")

with st.spinner("Computing L1 scores…"):
    scores_l1 = build_score(use_l2=False, use_lift=use_lift, _items=items, _trans=trans)

net_l1 = build_pyvis_graph(scores_l1, top_n=top_n, min_score=min_score)
render_graph(net_l1, key="l1")

st.subheader("Top pairs")
st.dataframe(
    scores_l1.select(["A", "B", "score", "lift"]).head(top_n).to_pandas(),
    use_container_width=True,
    height=400,
)

st.divider()

# ── Section 2: L2 categories ─────────────────────────────────
st.header("Sub Categories (L1 + L2)")
highlight_same_l1 = st.toggle("Highlight same-L1 edges with a different color", value=False)

with st.spinner("Computing L2 scores…"):
    scores_l2 = build_score(use_l2=True, use_lift=use_lift, _items=items, _trans=trans)

net_l2 = build_pyvis_graph(scores_l2, top_n=top_n, min_score=min_score, highlight_same_l1=highlight_same_l1)
render_graph(net_l2, key="l2")

st.subheader("Top pairs")
st.dataframe(
    scores_l2.select(["A", "B", "score", "lift"]).head(top_n).to_pandas(),
    use_container_width=True,
    height=400,
) 