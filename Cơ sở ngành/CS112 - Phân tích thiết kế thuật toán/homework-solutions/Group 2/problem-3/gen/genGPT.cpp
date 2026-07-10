#include "../testlib.h"
#include "bits/stdc++.h"
using namespace std;

int main(int argc, char **argv) {
    registerGen(argc, argv, 1);
    int type = atoi(argv[1]);
    long long seed = atoll(argv[2]);
    rnd.setSeed(seed);

    int n, m;
    vector<pair<int,int>> edges;

    auto add_edge = [&](int u, int v) {
        if (u == v) return;
        if (u > v) swap(u, v);
        if (find(edges.begin(), edges.end(), make_pair(u, v)) == edges.end())
            edges.push_back({u, v});
    };

    if (type == 1) { // Complete graph
        n = rnd.next(4, 7);
        for (int i = 1; i <= n; i++)
            for (int j = i + 1; j <= n; j++)
                add_edge(i, j);
    }

    else if (type == 2) { // Disconnected
        n = rnd.next(5, 8);
        for (int i = 1; i < n / 2; i++) add_edge(i, i + 1);
        for (int i = n / 2 + 1; i < n; i++) add_edge(i, i + 1);
    }

    else if (type == 3) { // Line graph
        n = rnd.next(4, 7);
        for (int i = 1; i < n; i++) add_edge(i, i + 1);
    }

    else if (type == 4) { // Star graph
        n = rnd.next(4, 7);
        for (int i = 2; i <= n; i++) add_edge(1, i);
    }

    else if (type == 5) { // Cycle
        n = rnd.next(4, 7);
        for (int i = 1; i < n; i++) add_edge(i, i + 1);
        add_edge(n, 1);
    }

    else if (type == 6) { // Almost-complete
        n = rnd.next(5, 8);
        for (int i = 1; i <= n; i++)
            for (int j = i + 1; j <= n; j++)
                add_edge(i, j);
        if (!edges.empty()) edges.erase(edges.begin() + rnd.next(0, (int)edges.size() - 1));
    }

    else if (type == 7) { // Random dense
        n = rnd.next(8, 10);
        int max_m = n * (n - 1) / 2;
        m = rnd.next(n, max_m / 3);
        set<pair<int,int>> used;
        while ((int)used.size() < m) {
            int u = rnd.next(1, n);
            int v = rnd.next(1, n);
            if (u == v) continue;
            if (u > v) swap(u, v);
            used.insert({u, v});
        }
        edges.assign(used.begin(), used.end());
    }

    else if (type == 8) { // Minimal 2 nodes
        n = 2;
        add_edge(1, 2);
    }

    else if (type == 9) { // Single node
        n = 1;
    }

    else if (type == 10) { // Two components
        n = rnd.next(6, 10);
        int mid = n / 2;
        for (int i = 1; i < mid; i++) add_edge(i, i + 1);
        for (int i = mid + 1; i < n; i++) add_edge(i, i + 1);
    }

    else if (type == 11) { // Oversized test to catch int/unsigned bugs (use in internal testing only)
        n = 100000; // intentionally outside constraints
        for (int i = 1; i <= 5; ++i) add_edge(i, i+1);
    }

    m = (int)edges.size();
    cout << n << " " << m << "\n";
    for (auto [u, v] : edges) cout << u << " " << v << "\n";
}
