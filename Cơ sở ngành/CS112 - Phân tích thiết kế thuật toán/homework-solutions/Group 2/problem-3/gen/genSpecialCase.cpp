#include "../testlib.h"
#include <bits/stdc++.h>
using namespace std;

void genLineGraph(int n) {
    cout << n << " " << n-1 << "\n";
    for (int i = 1; i < n; i++)
        cout << i << " " << i+1 << "\n";
}

void genCycleGraph(int n) {
    cout << n << " " << n << "\n";
    for (int i = 1; i < n; i++)
        cout << i << " " << i+1 << "\n";
    cout << n << " " << 1 << "\n";
}

void genAlmostComplete(int n) {
    vector<pair<int,int>> edges;
    for (int i = 1; i <= n; i++)
        for (int j = i+1; j <= n; j++)
            edges.push_back({i,j});
    shuffle(edges.begin(), edges.end());
    edges.pop_back(); // xóa 1 cạnh -> vẫn có Hamilton path
    cout << n << " " << edges.size() << "\n";
    for (auto [u,v] : edges)
        cout << u << " " << v << "\n";
}

void genDisconnected(int n) {
    // hai thành phần tách biệt
    int m = n/2 - 1;
    cout << n << " " << m << "\n";
    for (int i = 1; i < n/2; i++)
        cout << i << " " << i+1 << "\n";
}

void genStarWithCenterHighIndex(int n) {
    // Star nhưng tâm là đỉnh n -> bắt lỗi ai assume center=1
    cout << n << " " << n-1 << "\n";
    for (int i = 1; i < n; ++i) cout << i << " " << n << "\n";
}

void genTwoComponentsUnequal(int n) {
    // hai component: một rất nhỏ, một rất lớn (test greedy)
    int a = 2, b = n - a;
    cout << n << " " << (a-1) + (b-1) << "\n";
    for (int i = 1; i < a; ++i) cout << i << " " << i+1 << "\n";
    for (int i = a+1; i < n; ++i) cout << i << " " << i+1 << "\n";
}

void genSpecialCase(int type) {
    if (type == 1) genLineGraph(6);
    else if (type == 2) genCycleGraph(8);
    else if (type == 3) genAlmostComplete(10);
    else if (type == 4) genDisconnected(10);
    else if (type == 5) genStarWithCenterHighIndex(9);
    else genTwoComponentsUnequal(10);
}

int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);
    int type = atoi(argv[1]);
    int seed = atoi(argv[2]);
    rnd.setSeed(seed);
    genSpecialCase(type);
}
