import sys
input = sys.stdin.readline

INF = 200 ** 1000

if __name__ == "__main__":
    n = int(input())
    v = []
    for i in range(n):
        a, b, c = map(int, input().split())
        v.append((a, b, c))

    res = -INF
    for mask in range(1, 1 << n):

        chosen = []
        for i in range(n):
            if (mask >> i) & 1:
                chosen.append(v[i])
        
        chosen.sort()

        check = True
        for i in range(1, len(chosen)):
            if chosen[i-1][0] > chosen[i][0] or chosen[i-1][1] > chosen[i][1]:
                check = False
                break
        
        if check:
            cur = 1
            for w in chosen:
                cur *= w[2]

            res = max(res, cur)
    
    print(res)


# 5
# 1 7 -10
# 2 8 10
# 3 11 -7
# 4 12 -4
# 5 15 0

# 7
# 23 7 10
# 20 13 30
# 28 13 25
# 21 11 7
# 25 6 9
# 26 9 15
# 20 17 36