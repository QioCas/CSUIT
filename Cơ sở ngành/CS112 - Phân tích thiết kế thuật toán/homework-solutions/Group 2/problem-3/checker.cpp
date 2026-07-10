#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    int n = inf.readInt();
    int m = inf.readInt();
    vector<vector<int>> adj(n + 1, vector<int>(n + 1, 0));

    for (int i = 0; i < m; i++) {
        int u = inf.readInt();
        int v = inf.readInt();
        adj[u][v] = adj[v][u] = 1;
    }

    // Đọc output đúng và output thí sinh
    string ans_first = ans.readToken();
    string ouf_first = ouf.readToken();

    if (ans_first == "-1") {
        // Trường hợp không có đường đi Hamilton
        if (ouf_first != "-1")
            quitf(_wa, "Expected -1 (no Hamiltonian path), but contestant output something else");
        quitf(_ok, "Both outputs -1 (no path)");
    }

    // Nếu output đúng là 1 dãy đỉnh
    vector<int> correct(n);
    correct[0] = stoi(ans_first);
    for (int i = 1; i < n; i++)
        correct[i] = ans.readInt();

    vector<int> contestant;
    contestant.push_back(stoi(ouf_first));
    for (int i = 1; i < n; i++)
        contestant.push_back(ouf.readInt());

        
        // Kiểm tra tính hợp lệ của output thí sinh
        vector<bool> used(n + 1, false);
        for (int i = 0; i < n; i++) {
            int u = contestant[i];
            if (u < 1 || u > n)
            quitf(_wa, "Vertex %d out of range [1, %d]", u, n);
            if (used[u])
            quitf(_wa, "Vertex %d appears multiple times", u);
            used[u] = true;
            if (i > 0 && !adj[contestant[i - 1]][u])
            quitf(_wa, "No edge between %d and %d", contestant[i - 1], u);
        }
    ouf.readEof();
    quitf(_ok, "Valid Hamiltonian path");

}
