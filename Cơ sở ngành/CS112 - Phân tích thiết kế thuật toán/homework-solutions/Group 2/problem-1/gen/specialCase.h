void genSpecialCase(int cas) {
    n = rnd.next(max(1, maxN-10), maxN);
    for(int i = 0; i < n; ++i) {
        if(cas == 1) {
            a[i] = 0;
        } else if(cas == 2) {
            a[i] = rnd.next(maxA-10, maxA);
        } else if(cas == 3) {
            a[i] = rnd.next(minA, minA+10);
        } else {
            a[i] = (i & 1 ? rnd.next(1, maxA) : rnd.next(minA, -1));
        }
    }
    print();
}
