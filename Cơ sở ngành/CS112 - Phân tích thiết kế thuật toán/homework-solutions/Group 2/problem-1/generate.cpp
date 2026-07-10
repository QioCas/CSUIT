#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

int n, a[100005];
int type = -1, seed = -1, cas = -1, maxN = -1, minA = -1, maxA = -1;

void print() {
    assert(n > 0);

    cout << n << "\n";
    for(int i = 0; i < n; ++i) {
        cout << a[i] << " \n"[i==n-1];
    }
    
    for(int i = 0; i < n; ++i) a[i] = 0;
    n = 0;
}

#include "gen/normalCase.h"
#include "gen/specialCase.h"
#include "gen/edgeCase.h"
#include "gen/stressCase.h"

int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);
    type = opt<int>("type");
    seed = opt<int>("seed");
    cas = opt<int>("cas");
    maxN = opt<int>("maxN");
    maxA = opt<int>("maxA");
    minA = opt<int>("minA");

    rnd.setSeed(seed);

    if(type == 1) {
        genNormalCase();
    } else if(type == 2) {
        genSpecialCase(cas);
    } else if(type == 3) {
        genEdgeCase(cas);
    } else if(type == 4) {
        genStressCase(cas);
    }
    return 0;
}
