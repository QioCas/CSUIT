#include "../testlib.h"
#include "bits/stdc++.h"
using namespace std;

const int N_MAX = 100000;
const int M_MAX = 200000;
const int C_MAX = 1000000000;

int main(int argc, char **argv) {
    registerGen(argc, argv, 1);
    long long seed = atoll(argv[2]);
    rnd.setSeed(seed);

    int n = N_MAX;
    int m = M_MAX;
    cout << n << " " << m << "\n";

    for (int i = 0; i < m; ++i) {
        int u = rnd.next(1, n);
        int v = rnd.next(1, n);
        long long w = rnd.next(1, C_MAX);
        cout << u << " " << v << " " << w << "\n";
    }
}
