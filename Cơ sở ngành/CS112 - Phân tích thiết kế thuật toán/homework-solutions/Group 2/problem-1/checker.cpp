#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    // Đọc input
    int n = inf.readInt();
    for (int i = 0; i < n; i++) {
        int x = inf.readInt();
    }

    // Đọc output đúng (từ lời giải chính)
    long long expected = ans.readLong();
    // Đọc output của thí sinh
    long long contestant = ouf.readLong();

    
    ouf.readEof();
    // So sánh
    if (contestant != expected) {
        quitf(_wa, "Expected %lld, found %lld", expected, contestant);
    }
    
    // Nếu khớp
    quitf(_ok, "Correct answer: %lld", contestant);
}
