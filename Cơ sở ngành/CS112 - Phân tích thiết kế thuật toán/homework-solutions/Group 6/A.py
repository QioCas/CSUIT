import sys, time, heapq, random

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))

    r = [0]*n
    d = [0]*n
    p = [0]*n
    for i in range(n):
        r[i] = int(next(it)); d[i] = int(next(it)); p[i] = int(next(it))

    edd = sorted(range(n), key=lambda i: (d[i], r[i]))

    # exact for n <= 20
    if n <= 20:
        rem = [0]*(n+1)
        s = 0
        for i in range(n-1, -1, -1):
            s += p[edd[i]]
            rem[i] = s

        bestP = 0
        bestM = 0

        def dfs(i, t, pr, m):
            nonlocal bestP, bestM
            if pr + rem[i] <= bestP:
                return
            if pr > bestP:
                bestP, bestM = pr, m
            if i == n:
                return
            j = edd[i]
            if t + r[j] <= d[j]:
                dfs(i + 1, t + r[j], pr + p[j], m | (1 << i))
            dfs(i + 1, t, pr, m)

        dfs(0, 0, 0, 0)
        ans = [str(edd[i] + 1) for i in range(n) if (bestM >> i) & 1]
        sys.stdout.write(str(bestP) + "\n" + (" ".join(ans) if ans else "") + "\n")
        return

    ok = [r[i] <= d[i] for i in range(n)]
    rng = random.Random(1234567)

    presets = [
        (1.0, 1.0, 0.00),
        (1.0, 0.0, 0.00),
        (0.0, 1.0, 0.00),
        (1.4, 1.0, 0.04),
        (1.8, 1.2, 0.06),
        (2.2, 1.6, 0.08),
        (1.0, 2.0, 0.08),
    ]

    def run_once(A, B, nz):
        tt = 0
        pr = 0
        h = []
        for j in edd:
            if not ok[j]:
                continue
            sc = (p[j] ** A) / (r[j] ** B)
            if nz:
                sc *= 1.0 + (rng.random() * 2.0 - 1.0) * nz
            heapq.heappush(h, (sc, j))
            tt += r[j]
            pr += p[j]
            while tt > d[j]:
                _, k = heapq.heappop(h)
                tt -= r[k]
                pr -= p[k]
        return pr, h

    bestP = 0
    best_set = []

    end_time = time.perf_counter() + 4.8
    i = 0

    while time.perf_counter() < end_time:
        if i < len(presets):
            A, B, nz = presets[i]
        else:
            A = 0.5 + 3.5 * rng.random()
            B = 0.5 + 3.5 * rng.random()
            nz = 0.0 if rng.random() < 0.65 else 0.30 * rng.random()
        i += 1

        pr, h = run_once(A, B, nz)
        if pr > bestP:
            bestP = pr
            best_set = [idx for _, idx in h]

    chosen = [0]*n
    for j in best_set:
        chosen[j] = 1

    ans = [str(i + 1) for i in edd if chosen[i]]
    sys.stdout.write(str(bestP) + "\n" + " ".join(ans) + "\n")

if __name__ == "__main__":
    solve()
