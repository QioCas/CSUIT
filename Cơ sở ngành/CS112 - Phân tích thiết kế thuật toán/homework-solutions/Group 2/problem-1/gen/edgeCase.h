void genEdgeCase(int cas) {
    n = maxN;

    for (int i = 0; i < n; ++i) {
        if (cas == 1) {
            a[i] = minA;
        } else if (cas == 2) {
            a[i] = maxA;
        } else if (cas == 3) {
            a[i] = 0;
        } else {
            a[i] = rnd.next(minA, maxA);
        }
    }

    print();
}