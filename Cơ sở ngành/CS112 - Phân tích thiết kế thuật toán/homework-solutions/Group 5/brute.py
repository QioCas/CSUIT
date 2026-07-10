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

for i in range(q):
    u, v = map(int, input().split())
    u = u - 1
    v = v - 1
    ans = INF
    if u == v:
        ans = 0
    elif ms[u] & ms[v]:
        ans = abs(u-v)
    else:
        for k in range(n):
            if ms[k] & ms[u] and ms[k] & ms[v]:
                ans = min(ans, abs(u - k), abs(k - v))
    print(ans)

"""
4 5 
BR BR GY GR 
1 2
3 1
4 4
1 4
4 2
"""  
