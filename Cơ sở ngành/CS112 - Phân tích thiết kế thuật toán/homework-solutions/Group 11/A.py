import sys

input = sys.stdin.readline

if __name__ == "__main__":

    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(a[0])
        exit()
    
    dp = [0] * n
    dp[0] = a[0]
    dp[1] = max(a[0], a[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + a[i])
    print(dp[n-1])