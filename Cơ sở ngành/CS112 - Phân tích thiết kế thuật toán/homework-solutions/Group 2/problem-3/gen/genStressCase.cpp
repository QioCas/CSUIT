#include "../testlib.h"
#include <bits/stdc++.h>
using namespace std;

void genStressCase() {
    int n = 12;
    vector<pair<int,int>> edges;
    vector<vector<int>> adj(n+1, vector<int>(n+1, 0));

    int m = rnd.next(n*(n-1)/4, n*(n-1)/2);
    while ((int)edges.size() < m) {
        int u = rnd.next(1, n);
        int v = rnd.next(1, n);
        if (u == v || adj[u][v]) continue;
        adj[u][v] = adj[v][u] = 1;
        edges.push_back({u,v});
    }

    cout << n << " " << m << "\n";
    for (auto [u,v] : edges)
        cout << u << " " << v << "\n";
}

void genWorstCaseForBruteforce() {
    int n = 12;
    vector<pair<int,int>> edges;
    for (int i = 1; i <= n; ++i)
        for (int j = i+1; j <= n; ++j)
            if ((i + j) % 5 != 0) // remove some pattern to foil heuristics
                edges.push_back({i,j});
    cout << n << " " << edges.size() << "\n";
    for (auto &e: edges) cout << e.first << " " << e.second << "\n";
}

int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);
    int type = atoi(argv[1]);
    int seed = atoi(argv[2]);
    rnd.setSeed(seed);
    if (type == 1) genStressCase();
    else genWorstCaseForBruteforce();
}
