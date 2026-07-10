#include <bits/stdc++.h>

using namespace std;

const int maxN = 500500;

int n, m;

// Lưu đồ thị G
vector<int> G[maxN << 1];

// Lấy giá trị phủ định của x
int NOT(int x) {
    return x + (x <= n ? n : -n); // -x
}

// Thêm điều kiện u OR v
void add_clause_or(int u, int v) {
    G[NOT(u)].push_back(v); // -u -> v
    G[NOT(v)].push_back(u); // -v -> u
}

// Thêm điều kiện u AND v
void add_clause_and(int u, int v) {
    G[u].push_back(v); // u -> v
    G[v].push_back(u); // v -> u
}

// Tìm thành phần liên thông mạnh
int id[maxN << 1];
int num[maxN << 1], low[maxN << 1];
int timeDFS = 0, scc = 0;
int st[maxN << 1];

void dfs(int u) {
    num[u] = low[u] = ++timeDFS;
    st[++st[0]] = u;
    for(const int& v : G[u]) {
        if(id[v] != 0) continue;
        if(num[v] == 0) {
            dfs(v);
            low[u] = min(low[u], low[v]);
        } else low[u] = min(low[u], num[v]);
    }

    if(num[u] == low[u]) {
        for(++scc; true; ) {
            int v = st[st[0]--];
            id[v] = scc;
            if(v == u) break;
        }
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    cin >> n >> m;
    for(int i = 1; i <= m; ++i) {
        int t; cin >> t;
        int u, v; cin >> u >> v;
        if(t == 1) {
            // u & v | !u & !v
            add_clause_and(u, v);
            add_clause_and(NOT(u), NOT(v));
        } else {
            // u & !v | u & !v
            add_clause_and(NOT(u), v);
            add_clause_and(u, NOT(v));
        }
    }

    // Thuật toán Tarjan
    for(int i = 1; i <= 2 * n; ++i) {
        if(!id[i]) dfs(i);
    }

    bool answer = 1;
    for(int i = 1; i <= n; ++i) {
        // Kiểm tra điều kiện tồn tại phương án
        if(id[i] == id[NOT(i)]) answer = 0;
    }
    cout << (answer ? "NO\n" : "YES\n");
    return 0;
}
