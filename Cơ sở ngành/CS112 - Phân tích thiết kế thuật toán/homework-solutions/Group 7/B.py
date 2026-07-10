#include <bits/stdc++.h>
using namespace std;

struct Node {
    int mx = 0;     // giá trị max trên đoạn
    int lazy = 0;   // lazy add
    int idx = 0;    // vị trí y đạt mx
};

struct Event {
    long long x;
    int type;   // +1 = add, -1 = remove
    int y1, y2;
};

vector<Node> st;

void build(int p, int l, int r) {
    if (l == r) {
        st[p].idx = l;
        return;
    }
    int m = (l + r) >> 1;
    build(p<<1, l, m);
    build(p<<1|1, m+1, r);
    st[p].idx = st[p<<1].idx;
}

void push(int p) {
    if (st[p].lazy != 0) {
        for (int c : {p<<1, p<<1|1}) {
            st[c].mx   += st[p].lazy;
            st[c].lazy += st[p].lazy;
        }
        st[p].lazy = 0;
    }
}

void pull(int p) {
    if (st[p<<1].mx >= st[p<<1|1].mx) {
        st[p].mx  = st[p<<1].mx;
        st[p].idx = st[p<<1].idx;
    } else {
        st[p].mx  = st[p<<1|1].mx;
        st[p].idx = st[p<<1|1].idx;
    }
}

void update(int p, int l, int r, int L, int R, int val) {
    if (r < L || R < l) return;
    if (L <= l && r <= R) {
        st[p].mx   += val;
        st[p].lazy += val;
        return;
    }
    push(p);
    int m = (l + r) >> 1;
    update(p<<1, l, m, L, R, val);
    update(p<<1|1, m+1, r, L, R, val);
    pull(p);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> L(n), V(n), R(n);
    vector<long long> ys;
    ys.reserve(2*n);

    for (int i = 0; i < n; ++i) {
        cin >> L[i] >> V[i] >> R[i];
        ys.push_back(V[i]);
        ys.push_back(R[i]);
    }

    // nén tọa độ y = {v_i, r_i}
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());
    auto getY = [&](long long y) {
        return int(lower_bound(ys.begin(), ys.end(), y) - ys.begin());
    };

    vector<Event> ev;
    ev.reserve(2*n);
    for (int i = 0; i < n; ++i) {
        int y1 = getY(V[i]);
        int y2 = getY(R[i]);
        ev.push_back({L[i], +1, y1, y2});
        ev.push_back({V[i], -1, y1, y2});
    }

    // sort theo x tăng dần, cùng x thì add (+1) trước remove (-1)
    sort(ev.begin(), ev.end(), [](const Event& a, const Event& b) {
        if (a.x != b.x) return a.x < b.x;
        return a.type > b.type;  // +1 > -1
    });

    int M = ys.size();
    st.assign(4*M, Node());
    build(1, 0, M-1);

    int bestCnt = 0;
    long long bestX = L[0];
    long long bestY = V[0];

    for (auto &e : ev) {
        update(1, 0, M-1, e.y1, e.y2, e.type);
        if (st[1].mx > bestCnt) {
            bestCnt = st[1].mx;
            bestX = e.x;                  // minV
            bestY = ys[st[1].idx];        // maxV
        }
    }

    // Khôi phục tập đẹp
    vector<int> ans;
    ans.reserve(bestCnt);
    for (int i = 0; i < n; ++i) {
        if (L[i] <= bestX && bestX <= V[i] &&
            V[i] <= bestY && bestY <= R[i]) {
            ans.push_back(i + 1); // 1-based index
        }
    }

    cout << (int)ans.size() << "\n";
    for (int i = 0; i < (int)ans.size(); ++i) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    cout << "\n";
    return 0;
}
