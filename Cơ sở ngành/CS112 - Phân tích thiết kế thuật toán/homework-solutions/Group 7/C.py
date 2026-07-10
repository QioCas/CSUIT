import sys
import heapq

input = sys.stdin.readline
INF = 10**30

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    c = [0] + list(map(int, input().split()))

    # attributes a[i][t]
    a = [[0]*(m+1)]
    vals = [[] for _ in range(m+1)]
    for i in range(1, n+1):
        row = [0] + list(map(int, input().split()))
        a.append(row)
        for t in range(1, m+1):
            vals[t].append((row[t], i))

    # rank[i][t] = rank of i in attribute t
    rank = [[0]*(m+1) for _ in range(n+1)]
    dec = [[0]*(n+1) for _ in range(m+1)]

    for t in range(1, m+1):
        vals[t].sort()
        for r, (_, idx) in enumerate(vals[t], 1):
            rank[idx][t] = r
            dec[t][r] = idx

    # dist[x][t] = min cost having pokemon x, using attribute t
    dist = [[INF]*(m+1) for _ in range(n+1)]
    vis = [0]*(n+1)

    pq = []
    for t in range(1, m+1):
        dist[1][t] = 0
        pq.append((0, 1, t))

    heapq.heapify(pq)
    ans = INF

    while pq:
        d, x, t = heapq.heappop(pq)
        if d != dist[x][t]:
            continue

        # If we reached pokemon n, final cost = d + c[n]
        if x == n:
            if d + c[n] < ans:
                ans = d + c[n]
            # Continue; do NOT break (different attributes may give cheaper)
        
        r = rank[x][t]

        # Move upward: (increase attribute cost = 0)
        if r < n:
            nxt = dec[t][r+1]
            if d < dist[nxt][t]:
                dist[nxt][t] = d
                heapq.heappush(pq, (d, nxt, t))

        # Move downward: cost = a[x][t] - a[nxt][t]
        if r > 1:
            nxt = dec[t][r-1]
            cost = d + (a[x][t] - a[nxt][t])
            if cost < dist[nxt][t]:
                dist[nxt][t] = cost
                heapq.heappush(pq, (cost, nxt, t))

        # Use pokemon x in all attributes (hire cost)
        if not vis[x]:
            vis[x] = 1
            hire = d + c[x]
            for tt in range(1, m+1):
                if hire < dist[x][tt]:
                    dist[x][tt] = hire
                    heapq.heappush(pq, (hire, x, tt))

    print(ans)
