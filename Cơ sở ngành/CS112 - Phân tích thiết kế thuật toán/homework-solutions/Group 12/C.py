import sys

def solve_one(p):
    n = len(p)
    # 0-based values
    p = [x - 1 for x in p]
    pos = [0] * n
    for i, v in enumerate(p):
        pos[v] = i

    m = 0
    while m <= n - 3:
        a = pos[m]
        b = pos[m + 1]
        c = pos[m + 2]

        if c < a and c < b:
            i = c
            j = a if a < b else b
            k = b if a < b else a

            # Apply operation (i<j<k, p[i]=m+2, {p[j],p[k]}={m,m+1})
            p[i] -= 2
            p[j] += 1
            p[k] += 1

            # Update positions for the 3 affected values
            pos[p[i]] = i
            pos[p[j]] = j
            pos[p[k]] = k

            # Re-check earlier triples (pointer walk)
            m = m - 2
            if m < 0:
                m = 0
        else:
            m += 1

    return [x + 1 for x in p]


def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]; idx += 1
        p = data[idx:idx+n]; idx += n
        ans = solve_one(p)
        out.append(" ".join(map(str, ans)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
