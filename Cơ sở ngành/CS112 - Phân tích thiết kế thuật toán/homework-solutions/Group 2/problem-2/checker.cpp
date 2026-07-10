#include "testlib.h"
#include "bits/stdc++.h"

long long read_ans(int n, InStream& stream) {
	long long dist = stream.readLong((long long) -1, (long long) 1000000000000000000);
    return dist;
}

int main(int argc, char *argv[]) {
	registerTestlibCmd(argc, argv);
	
	int n = inf.readInt();
	int m = inf.readInt();
    int s = 1, t = n;

    for (int i = 0; i < m; i++) {
        int a = inf.readInt();
        int b = inf.readInt();
        int c = inf.readInt();
    }

    long long res_correct = read_ans(n, ans);
    long long res_submitted = read_ans(n, ouf);

    ouf.readEof();

    if (res_correct != res_submitted) {
        quitf(_wa, "Wrong answer: expected %lld, found %lld", res_correct, res_submitted);
    }

    quitf(_ok, "OK");
}
