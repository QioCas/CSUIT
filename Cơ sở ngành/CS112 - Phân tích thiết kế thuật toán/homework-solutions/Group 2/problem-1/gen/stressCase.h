void genStressCase(int cas) {
    n = maxN;

    for(int i = 0; i < n; ++i) {
        if(cas == 1) {
            a[i] = maxA;
        } else if(cas == 2) {
            a[i] = minA;
        } else {
            a[i] = rnd.next(minA, maxA);
        }
    }

    print();
}
