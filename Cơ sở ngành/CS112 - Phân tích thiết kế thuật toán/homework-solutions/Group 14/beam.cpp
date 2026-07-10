#include <bits/stdc++.h>
using namespace std;

struct PathState {
    vector<int> path;   // đường đi hiện tại
    long long visitedMask; // đánh dấu các đỉnh đã đi bằng bitmask
};

mt19937 rng(time(NULL));

int randint(int l, int r) {
    return uniform_int_distribution<int>(l, r) (rng);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<vector<int>> g(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    if (N == 1) {
        cout << "0\n1\n";
        return 0;
    }

    // quick connectivity check
    vector<bool> reach(N + 1, false);
    queue<int> q;
    q.push(1); reach[1] = true;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : g[u]) if (!reach[v]) { reach[v] = true; q.push(v); }
    }
    if (!reach[N]) { cout << "-1\n"; return 0; }

    int beamWidth = 50000;
    vector<PathState> beam;
    PathState start; 
    start.path.push_back(1); start.visitedMask = 1LL << 0; // vertex 1
    beam.push_back(start);

    int bestLen = -1;
    vector<int> bestPath;

    while (!beam.empty()) {
        vector<PathState> nextBeam;

        for (auto &state : beam) {
            int u = state.path.back();
            if (u == N) {
                if ((int)state.path.size() > bestLen) {
                    bestLen = state.path.size();
                    bestPath = state.path;
                }
                continue;
            }
            for (int v : g[u]) {
                long long bit = 1LL << (v - 1);
                if (state.visitedMask & bit) continue; // đã đi rồi
                PathState ns;
                ns.path = state.path;
                ns.path.push_back(v);
                ns.visitedMask = state.visitedMask | bit;
                nextBeam.push_back(ns);
            }
        }

        sort(nextBeam.begin(), nextBeam.end(), [](const PathState &a, const PathState &b){
            if(a.path.size() != b.path.size()) return a.path.size() > b.path.size();
            if(a.visitedMask !=  b.visitedMask) return a.visitedMask < b.visitedMask;
            return a.path.back() < b.path.back();
        });
        for(int i = 1, j = 0; i < (int) nextBeam.size(); ++i) {
            if(nextBeam[j].visitedMask == nextBeam[i].visitedMask && nextBeam[j].path.back() == nextBeam[i].path.back()) {
                continue;
            } else nextBeam[++j] = nextBeam[i];
        }
        if ((int)nextBeam.size() > beamWidth) nextBeam.resize(beamWidth);

        beam = move(nextBeam);
    }

    if (bestLen == -1) cout << "-1\n";
    else {
        cout << bestLen - 1 << "\n";
        for (int i = 0; i < bestPath.size(); i++) {
            if (i) cout << " ";
            cout << bestPath[i];
        }
        cout << "\n";
    }
    return 0;
}
