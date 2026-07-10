import sys

input = sys.stdin.readline

code_str = "BGRY"
idx = {c: 1 << i for i, c in enumerate(code_str)}
INF = 1000000000

def get_idx(c):
    return idx[c]

n, q = map(int, input().split())
s = input().split()
ms = [get_idx(s[i][0]) | get_idx(s[i][1]) for i in range(n)]

last = [(-1, -1) for i in range(4)]
L = [-1 for i in range(n)]
R = [n for i in range(n)]

for i in range(n):
    for b in range(4):
        if ms[i] >> b & 1:
            p = last[b][last[b][0] != -1 and ms[i] == ms[last[b][0]]]
            if p != -1:
                L[i] = max(L[i], p)
                R[p] = min(R[p], i)

            if last[b][0] == -1 or ms[last[b][0]] == ms[i]:
                last[b] = (i, last[b][1])
            else: 
                last[b] = (i, last[b][0])

for i in range(q):
    u, v = map(int, input().split())
    u = u - 1
    v = v - 1
    ans = -1
    if ms[u] & ms[v]:
        ans = abs(u-v)
    else:
        ans = INF
        if L[u] != -1:
            ans = min(ans, abs(u - L[u]) + abs(L[u] - v))
        if R[u] != n:
            ans = min(ans, abs(u - R[u]) + abs(R[u] - v))
        if L[v] != -1:
            ans = min(ans, abs(v - L[v]) + abs(L[v] - u))
        if R[v] != n:
            ans = min(ans, abs(v - R[v]) + abs(R[v] - u))
        if ans == INF:
            ans = -1
    print(ans)
