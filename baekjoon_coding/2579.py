import sys

n = int(sys.stdin.readline())

stairs = [int(sys.stdin.readline().strip()) for _ in range(n)]

dp = [0] * n

if n == 1:
    print(stairs[0])

if n == 2:
    print(stairs[1])

else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
    
    print(dp[-1])