import sys

# ---------------- fast int reader ----------------
def ints():
    data = sys.stdin.buffer.read()
    n = len(data)
    i = 0
    while i < n:
        while i < n and data[i] <= 32:
            i += 1
        if i >= n:
            break
        sgn = 1
        if data[i] == 45:  # '-'
            sgn = -1
            i += 1
        x = 0
        while i < n and data[i] > 32:
            x = x * 10 + (data[i] - 48)
            i += 1
        yield sgn * x

# ---------------- Fenwick ----------------
class Fenwick:
    __slots__ = ("n", "b")
    def __init__(self, n):
        self.n = n
        self.b = [0] * (n + 1)

    def add(self, i, v):
        b = self.b
        n = self.n
        while i <= n:
            b[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        b = self.b
        while i:
            s += b[i]
            i -= i & -i
        return s

# tree-walk to find smallest idx i s.t. max(topL, botL) >= max(topR, botR)
# botL = totalL - topL, topR = topTot - topL, botR = botTot - botL
def find_cross(bitT, bitTop, topTot, botTot, m):
    bT = bitT.b
    bP = bitTop.b

    # predicate using prefix sums at i: (tL, totL)
    def pred(tL, totL):
        bL = totL - tL
        left = tL if tL >= bL else bL
        tR = topTot - tL
        bR = botTot - bL
        right = tR if tR >= bR else bR
        return left >= right

    # i = 0
    if pred(0, 0):
        return 0

    idx = 0
    tL = 0
    totL = 0
    step = 1 << (m.bit_length() - 1)

    while step:
        nxt = idx + step
        if nxt <= m:
            ntL = tL + bP[nxt]
            ntotL = totL + bT[nxt]
            if not pred(ntL, ntotL):
                idx = nxt
                tL = ntL
                totL = ntotL
        step >>= 1

    ans = idx + 1
    if ans > m:
        ans = m
    return ans

def solve():
    it = ints()
    H = next(it, None)
    if H is None:
        return
    W = next(it)
    n = next(it)

    if n == 0:
        sys.stdout.write("0")
        return
    if H < 2 or W < 2:
        # cannot place both cuts (between consecutive rows/cols)
        sys.stdout.write(str(n))
        return

    pts = [None] * n
    cols = [0] * n
    for i in range(n):
        r = next(it); c = next(it)
        pts[i] = (r, c)
        cols[i] = c

    # compress columns
    cols_sorted = sorted(set(cols))
    m = len(cols_sorted)
    col_id = {c: i + 1 for i, c in enumerate(cols_sorted)}  # 1-indexed

    # sort points by row for sweep
    pts.sort(key=lambda x: x[0])

    # BIT_total has all points fixed; BIT_top starts empty and grows as we move rows up
    bitTotal = Fenwick(m)
    bitTop = Fenwick(m)

    for r, c in pts:
        bitTotal.add(col_id[c], 1)

    topTot = 0
    botTot = n

    best = n

    def eval_vertical():
        nonlocal best
        k = find_cross(bitTotal, bitTop, topTot, botTot, m)
        # check k and k-1
        for i in (k - 1, k):
            if i < 0: 
                continue
            if i == 0:
                tL = 0
                totL = 0
            else:
                tL = bitTop.sum(i)
                totL = bitTotal.sum(i)
            bL = totL - tL
            tR = topTot - tL
            bR = botTot - bL
            mx = tL
            if tR > mx: mx = tR
            if bL > mx: mx = bL
            if bR > mx: mx = bR
            if mx < best:
                best = mx

    # cut before first occupied row (top has 0 points), only if there exists a row cut < min_row
    min_row = pts[0][0]
    if min_row > 1:
        eval_vertical()

    # sweep by row groups
    i = 0
    while i < n:
        r = pts[i][0]
        # move all points in this row to TOP
        while i < n and pts[i][0] == r:
            bitTop.add(col_id[pts[i][1]], 1)
            topTot += 1
            botTot -= 1
            i += 1

        # cut after row r is valid if r <= H-1
        if r <= H - 1:
            eval_vertical()

    sys.stdout.write(str(best))

if __name__ == "__main__":
    solve()
