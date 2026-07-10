#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<int> path;
vector<bool> used;
bool found = false;

void dfs(int u, int cnt) {
    if (found) return;
    if (cnt == n) {
        for (int i = 0; i < n; i++) {
            cout << path[i] << (i + 1 == n ? '\n' : ' ');
        }
        found = true;
        return;
    }
    for (int v = 1; v <= n; v++) {
        if (!used[v] && adj[u][v]) {
            used[v] = true;
            path.push_back(v);
            dfs(v, cnt + 1);
            path.pop_back();
            used[v] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    adj.assign(n + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u][v] = adj[v][u] = 1;
    }

    for (int start = 1; start <= n && !found; start++) {
        used.assign(n + 1, false);
        path.clear();
        path.push_back(start);
        used[start] = true;
        dfs(start, 1);
    }

    if (!found) cout << -1 << "\n";
}
