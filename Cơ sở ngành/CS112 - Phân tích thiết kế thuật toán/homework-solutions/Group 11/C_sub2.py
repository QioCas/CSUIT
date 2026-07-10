import sys

input = sys.stdin.readline

INF = 200 ** 1000

if __name__ == "__main__":
    n = int(input())
    
    dp_min = [INF] * (n + 1)
    dp_max = [-INF] * (n + 1)
    dp_max[0] = dp_min[0] = 1

    v = []
    v.append((0, 0, 1))
    for i in range(1,  n + 1):
        a, b, c = map(int, input().split())
        v.append((a, b, c))

    v.sort()
    
    
    res = -INF
    for i in range(1, n + 1):
        a, b, c = v[i]
        for j in range(0, i):
            if (v[j][0] <= v[i][0] and v[j][1] <= v[i][1]):
                dp_max[i] = max(dp_max[i], dp_max[j] * c)
                dp_max[i] = max(dp_max[i], dp_min[j] * c)

                dp_min[i] = min(dp_min[i], dp_max[j] * c)
                dp_min[i] = min(dp_min[i], dp_min[j] * c)

        # print(dp_max[i], dp_min[i])
        res = max(res, dp_max[i])

    print(res)