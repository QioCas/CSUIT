#include "testlib.h"
#include "bits/stdc++.h"

const int N_MIN = 2;
const int N_MAX = 100000;
const int M_MIN = 0;
const int M_MAX = 200000;
const int C_MIN = 1;
const int C_MAX = 1e9;

int main(int argc, char* argv[]) {
	registerValidation(argc, argv);
	
	int n = inf.readInt(N_MIN, N_MAX);
	inf.readSpace();
	int m = inf.readInt(M_MIN, M_MAX);
	inf.readChar('\n');
	
	std::set<std::pair<int, int> > hens;
	for (int i = 0; i < m; i++) {
		int a = inf.readInt(1, n);
		inf.readSpace();
		int b = inf.readInt(1, n);
		inf.readSpace();
		inf.readInt(C_MIN, C_MAX, "c");
		inf.readChar('\n');
	}
	inf.readEof();
	return 0;
}