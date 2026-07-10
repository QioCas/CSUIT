import sys

INF = 10**18

# ---------------- Fenwick (BIT) ----------------
class Fenwick:
    __slots__ = ("n", "bit")
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        bit = self.bit
        n = self.n
        while i <= n:
            bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def kth(self, k: int) -> int:
        """Return smallest idx such that prefix_sum(idx) >= k (1-indexed k)."""
        idx = 0
        bitmask = 1 << (self.n.bit_length() - 1)
        bit = self.bit
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and bit[nxt] < k:
                k -= bit[nxt]
                idx = nxt
            bitmask >>= 1
        return idx + 1

# ---------------- Solution ----------------
def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(map(int, data))
    N = next(it)
    M = next(it)

    start = [0] * (N + 1)
    commit = [0] * (N + 1)

    events = []  # (time, type, id) where type: 0=remove, 1=add, 2=query
    # type order doesn't matter because all timestamps (except -1) are distinct

    for t in range(1, N + 1):
        s = next(it); c = next(it)
        start[t] = s
        commit[t] = c
        events.append((s, 2, t))  # query at start_time[t]

    # tuple j exists in [commit(create_tx), commit(delete_tx)) with aborted tx ignored
    for j in range(1, M + 1):
        c_tx = next(it)
        d_tx = next(it)

        # creation commit
        if c_tx < 1 or c_tx > N:
            continue
        c_time = commit[c_tx]
        if c_time == -1:
            continue  # never created -> never exists

        # deletion commit
        if d_tx == -1:
            d_time = INF
        else:
            if d_tx < 1 or d_tx > N:
                d_time = INF
            else:
                d_time = commit[d_tx]
                if d_time == -1:
                    d_time = INF  # aborted delete -> not deleted

        events.append((c_time, 1, j))   # add at create commit
        if d_time != INF:
            events.append((d_time, 0, j))  # remove at delete commit

    events.sort(key=lambda x: x[0])

    bit = Fenwick(M)
    out = [""] * (N + 1)

    for time, typ, idx in events:
        if typ == 1:
            bit.add(idx, 1)
        elif typ == 0:
            bit.add(idx, -1)
        else:
            k = bit.sum(M)
            if k == 0:
                out[idx] = "0"
            else:
                res = [str(k)]
                for t in range(1, k + 1):
                    res.append(str(bit.kth(t)))
                out[idx] = " ".join(res)

    sys.stdout.write("\n".join(out[1:]))

if __name__ == "__main__":
    solve()
