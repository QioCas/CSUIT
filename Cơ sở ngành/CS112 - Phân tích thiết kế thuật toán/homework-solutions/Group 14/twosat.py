import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    def NOT(x):
        return x + n if x <= n else x - n

    size = 2 * n + 5
    G = [[] for _ in range(size)]
    id_scc = [0] * size
    num = [0] * size
    low = [0] * size
    stack = [0] * size
    
    timeDFS = 0
    scc = 0

    def dfs(u):
        nonlocal timeDFS, scc
        timeDFS += 1
        num[u] = low[u] = timeDFS
        stack[0] += 1
        stack[stack[0]] = u

        for v in G[u]:
            if id_scc[v] != 0:
                continue
            if num[v] == 0:
                dfs(v)
                low[u] = min(low[u], low[v])
            else:
                low[u] = min(low[u], num[v])

        if num[u] == low[u]:
            scc += 1
            while True:
                v = stack[stack[0]]
                stack[0] -= 1
                id_scc[v] = scc
                if v == u:
                    break

    def add_clause_and(u, v):
        G[u].append(v)
        G[v].append(u)

    for _ in range(m):
        t = int(next(it))
        u = int(next(it))
        v = int(next(it))
        if t == 1:
            add_clause_and(u, v)
            add_clause_and(NOT(u), NOT(v))
        else:
            add_clause_and(NOT(u), v)
            add_clause_and(u, NOT(v))

    for i in range(1, 2 * n + 1):
        if id_scc[i] == 0:
            dfs(i)

    valid = True
    for i in range(1, n + 1):
        if id_scc[i] == id_scc[NOT(i)]:
            valid = False

    print("NO" if valid else "YES")


if __name__ == "__main__":
    main()
