import sys
from bisect import bisect_right, bisect_left, insort

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    W = next(it); H = next(it)
    n = next(it); m = next(it)

    rects = []
    for i in range(n):
        X = next(it); Y = next(it); A = next(it); B = next(it)
        # ensure X < A and Y < B (problem statement guarantees)
        rects.append((X, Y, A, B, i))

    hunters = []
    for j in range(m):
        C = next(it); R = next(it); t = next(it)
        hunters.append((C, R, t, j))

    # events: (x, type, ...), type order: 0=open,1=query,2=close
    # open: (Xi,0,Yi,Bi,idx)
    # query: (Cj,1,Rj,tj,j)
    # close: (Ai,2,Yi,Bi,idx)
    events = []
    for (X,Y,A,B,i) in rects:
        events.append((X, 0, Y, B, i))
        events.append((A, 2, Y, B, i))
    for (C,R,t,j) in hunters:
        events.append((C, 1, R, t, j))

    # sort by x, then type (open -> query -> close)
    events.sort(key=lambda e: (e[0], e[1]))

    # active intervals sorted by Yi: store tuples (Yi, Bi, idx)
    active = []  # maintained sorted by Yi

    ans = [0] * (n + 1)  # ans[0..n-1] for rectangles, ans[n] for outside

    for ev in events:
        typ = ev[1]
        if typ == 0:
            # open
            _,_, Yi, Bi, idx = ev
            insort(active, (Yi, Bi, idx))
        elif typ == 2:
            # close -> remove (Yi,Bi,idx)
            _,_, Yi, Bi, idx = ev
            # find position of (Yi, Bi, idx)
            pos = bisect_left(active, (Yi, Bi, idx))
            # robust removal: scan neighbors if equal Yi but different Bi/idx
            # but since we inserted exactly same tuple, bisect_left should find it
            if pos < len(active) and active[pos] == (Yi, Bi, idx):
                active.pop(pos)
            else:
                # fallback: linear search (should not happen normally)
                for k in range(len(active)):
                    if active[k][0] == Yi and active[k][1] == Bi and active[k][2] == idx:
                        active.pop(k)
                        break
        else:
            # query
            _,_, Rj, tj, _ = ev
            # find rightmost interval with Yi <= Rj
            pos = bisect_right(active, (Rj, 10**30, 10**30)) - 1
            if pos >= 0:
                Yi, Bi, idx = active[pos]
                # check if Rj is inside vertical interval
                # currently using strict inclusion: Yi < Rj < Bi
                if Yi < Rj < Bi:
                    ans[idx] += tj
                else:
                    ans[n] += tj
            else:
                ans[n] += tj

    # print results: n numbers for rectangles (index 0..n-1 in original input order), then outside
    out = " ".join(str(ans[i]) for i in range(n)) + " " + str(ans[n])
    print(out)

if __name__ == "__main__":
    main()
