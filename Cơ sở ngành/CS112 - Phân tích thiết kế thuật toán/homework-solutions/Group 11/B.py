import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, W = map(int, input().split())
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))

    dp = [0] * (W + 1)

    for i in range(n):
        wi = weights[i]
        vi = values[i]

        for w in range(W, wi - 1, -1):
            dp[w] = max(dp[w], dp[w - wi] + vi)
    
    print(max(dp))