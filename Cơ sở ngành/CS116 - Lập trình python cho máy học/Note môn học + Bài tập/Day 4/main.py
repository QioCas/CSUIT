import streamlit as st
import polars as pl

st.title("Item Matcher")

@st.cache_data
def load_items():
    return pl.read_parquet("./items.parquet")

df = load_items()

item_id_col = "item_id"

weights = {
    "category_l1": 0.05,
    "category_l2": 0.20,
    "category_l3": 0.25,
    "category": 0.30,
    "price": 0.20,
}

def top_k_matches_full(df: pl.DataFrame, query_item_ids: list[str], k: int = 100) -> pl.DataFrame:
    exact_match_cols = ["category_l1", "category_l2", "category_l3", "category"]

    query_item_ids = [str(x).strip() for x in query_item_ids if str(x).strip()]
    query_ids_series = pl.Series("query_item_id", query_item_ids, dtype=pl.String)

    queries = (
        df.filter(pl.col(item_id_col).is_in(query_ids_series))
        .select(
            [pl.col(item_id_col).alias("query_item_id")] +
            [pl.col(c).alias(f"q_{c}") for c in exact_match_cols] +
            [pl.col("price").cast(pl.Float64).alias("q_price")]
        )
    )

    candidates = df.rename({col: f"cand_{col}" for col in df.columns}).with_columns(
        pl.col("cand_price").cast(pl.Float64)
    )

    exact_score_expr = sum(
        (pl.col(f"q_{c}") == pl.col(f"cand_{c}")).cast(pl.Float64) * weights[c]
        for c in exact_match_cols
    )

    price_sim_expr = (
        pl.when(
            (pl.col("q_price").is_not_null()) &
            (pl.col("cand_price").is_not_null()) &
            (pl.max_horizontal("q_price", "cand_price") > 0)
        )
        .then(
            1.0 - (
                (pl.col("q_price") - pl.col("cand_price")).abs() /
                pl.max_horizontal("q_price", "cand_price")
            )
        )
        .otherwise(0.0)
        .clip(0.0, 1.0)
    )

    score_expr = (
        exact_score_expr + price_sim_expr * weights["price"]
    ).alias("score")

    result = (
        queries.lazy()
        .join(candidates.lazy(), how="cross")
        .filter(pl.col("query_item_id") != pl.col(f"cand_{item_id_col}"))
        .with_columns(score_expr)
        .sort(
            ["query_item_id", "score", f"cand_{item_id_col}"],
            descending=[False, True, False]
        )
        .group_by("query_item_id", maintain_order=True)
        .head(k)
        .collect()
    )

    return result

st.write("Sample items:")
st.dataframe(df.head(), use_container_width=True)

st.write("Items schema:")
st.write(df.schema)

# Random sample for dropdown
sample_df = df.sample(n=min(100, df.height), seed=42).select(
    [
        pl.col(item_id_col),
        pl.col("brand"),
        pl.col("category"),
        pl.col("price").cast(pl.Float64)
    ]
)

sample_rows = sample_df.to_dicts()

label_to_id = {
    f"{row['item_id']} | {row['brand'] or 'N/A'} | {row['category'] or 'N/A'} | {row['price']:.2f}" if row["price"] is not None
    else f"{row['item_id']} | {row['brand'] or 'N/A'} | {row['category'] or 'N/A'} | N/A": row["item_id"]
    for row in sample_rows
}

selected_label = st.selectbox(
    "Choose an item",
    options=list(label_to_id.keys())
)

selected_item_id = label_to_id[selected_label]

k = st.number_input("Top K matches", min_value=1, max_value=1000, value=100, step=1)

if st.button("Find matches"):
    query_item_ids = [selected_item_id]

    found_queries = df.filter(pl.col(item_id_col).is_in(query_item_ids))

    if found_queries.height == 0:
        st.error("Selected item_id was not found in items.parquet.")
    else:
        found_ids = found_queries[item_id_col].to_list()
        result = top_k_matches_full(df, found_ids, k=int(k))

        if result.height == 0:
            st.info("No matches found.")
        else:
            for qid in found_ids:
                st.subheader(f"Input item: {qid}")

                input_item_df = df.filter(pl.col(item_id_col) == qid)
                st.write("Input item info:")
                st.dataframe(input_item_df, use_container_width=True)

                matched_df = (
                    result
                    .filter(pl.col("query_item_id") == qid)
                    .select(["score"] + [f"cand_{col}" for col in df.columns])
                    .rename({f"cand_{col}": col for col in df.columns})
                )

                st.write(f"Top {len(matched_df)} matched items:")
                st.dataframe(matched_df, use_container_width=True)