import sys

def ways_of_tiling(n):
    if n < 1 or n > 1000:
        return 0
    if n == 1:
        return 1
    
    dp = [0] * (n+1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    return dp[n]


n = int(sys.stdin.readline())

print(ways_of_tiling(n))
