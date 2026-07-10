import sys
import heapq

INF = 10**30

def solve_odd(n, a):
    # a is 1-indexed length 2n
    def idx_of_pos(pos):
        return pos if pos <= n else pos - n

    def get_val(pos, x):
        # x is swap bit of idx_of_pos(pos)
        if pos <= n:
            return a[pos] if x == 0 else a[pos + n]
        else:
            return a[pos] if x == 0 else a[pos - n]

    # Each desk = (2k-1, 2k) induces an edge between consecutive indices on 1..n (cyclic) when n is odd
    pos_e = [0] * (n + 1)
    pos_next = [0] * (n + 1)
    for k in range(1, n + 1):
        p1, p2 = 2 * k - 1, 2 * k
        u, v = idx_of_pos(p1), idx_of_pos(p2)
        if (u % n) + 1 == v:
            e = u
            pos_e[e], pos_next[e] = p1, p2
        else:
            e = v
            pos_e[e], pos_next[e] = p2, p1

    w = [[[0, 0], [0, 0]] for _ in range(n + 1)]
    for e in range(1, n + 1):
        pe, pn = pos_e[e], pos_next[e]
        w[e][0][0] = get_val(pe, 0) + get_val(pn, 0)
        w[e][0][1] = get_val(pe, 0) + get_val(pn, 1)
        w[e][1][0] = get_val(pe, 1) + get_val(pn, 0)
        w[e][1][1] = get_val(pe, 1) + get_val(pn, 1)

    def prune(pairs):
        # keep nondominated (mn high, mx low is better)
        if not pairs:
            return []
        best = {}
        for mn, mx in pairs:
            cur = best.get(mn)
            if cur is None or mx < cur:
                best[mn] = mx
        items = sorted(best.items(), key=lambda x: x[0], reverse=True)  # mn desc
        res, best_mx = [], INF
        for mn, mx in items:
            if mx < best_mx:
                res.append((mn, mx))
                best_mx = mx
        return res

    def apply_edge(frontier, weight):
        res = []
        for mn, mx in frontier:
            if mn == INF:
                res.append((weight, weight))
            else:
                res.append((mn if mn < weight else weight, mx if mx > weight else weight))
        return res

    ans = INF
    for s1 in (0, 1):
        dp0, dp1 = [], []
        (dp0 if s1 == 0 else dp1).append((INF, -1))

        for e in range(1, n):
            ndp0, ndp1 = [], []
            if dp0:
                ndp0 += apply_edge(dp0, w[e][0][0])
                ndp1 += apply_edge(dp0, w[e][0][1])
            if dp1:
                ndp0 += apply_edge(dp1, w[e][1][0])
                ndp1 += apply_edge(dp1, w[e][1][1])
            dp0, dp1 = prune(ndp0), prune(ndp1)

        e = n
        for sn, frontier in ((0, dp0), (1, dp1)):
            if not frontier:
                continue
            weight = w[e][sn][s1]
            for mn, mx in frontier:
                if mn == INF:
                    mn2 = mx2 = weight
                else:
                    mn2 = mn if mn < weight else weight
                    mx2 = mx if mx > weight else weight
                ans = min(ans, mx2 - mn2)
    return ans

def solve_even(n, a):
    # n even. Components: (u=2k-1, v=2k), each gives 4 intervals [mn,mx]
    m = n // 2
    options = []  # (mn, mx, comp_id)

    for comp in range(m):
        u = 2 * comp + 1
        v = 2 * comp + 2
        Au, Bu = a[u], a[u + n]
        Av, Bv = a[v], a[v + n]

        # xu, xv in {0,1}; desk1 uses chosen, desk2 uses the other
        for xu in (0, 1):
            for xv in (0, 1):
                d1 = (Bu if xu else Au) + (Bv if xv else Av)
                d2 = (Au if xu else Bu) + (Av if xv else Bv)
                mn, mx = (d1, d2) if d1 <= d2 else (d2, d1)
                options.append((mn, mx, comp))

    # Sweep mn descending; maintain for each comp: best_mx = min mx among options with mn >= current L
    options.sort(reverse=True)  # by mn desc
    best_mx = [INF] * m
    covered = 0

    heap = []  # (-best_mx, comp) for max query with lazy deletion
    ans = INF
    i = 0
    while i < len(options):
        L = options[i][0]  # current mn threshold
        # add all options with this mn (since sorted desc, all with mn >= L are in prefix)
        while i < len(options) and options[i][0] == L:
            mn, mx, c = options[i]
            if mx < best_mx[c]:
                if best_mx[c] == INF:
                    covered += 1
                best_mx[c] = mx
                heapq.heappush(heap, (-mx, c))
            i += 1

        if covered == m:
            while heap:
                negmx, c = heap[0]
                if -negmx == best_mx[c]:
                    break
                heapq.heappop(heap)
            global_max = -heap[0][0]
            ans = min(ans, global_max - L)

    return ans

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ptr = 1
    out = []
    for _ in range(t):
        n = data[ptr]; ptr += 1
        arr = data[ptr:ptr + 2 * n]; ptr += 2 * n
        a = [0] + arr  # 1-index
        if n % 2 == 1:
            out.append(str(solve_odd(n, a)))
        else:
            out.append(str(solve_even(n, a)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
