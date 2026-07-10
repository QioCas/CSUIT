void genNormalCase() {
    n = rnd.next(max(1, maxN - 10), maxN);
    for(int i = 0; i < n; ++i) {
        a[i] = rnd.next(minA, maxA);
    }

    print();
}
