import sys

n = int(sys.stdin.readline())

stairs = [int(sys.stdin.readline().strip()) for _ in range(n)]
# [10, 20, 15, 25, 10, 20]

dp = [0] * n

if n <= 2:
    print(sum(stairs))

else:
    dp[0] = stairs[0]       #10
    dp[1] = stairs[0] + stairs[1]   #30

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

        # dp[2] = max(dp[0] + stairs[2], dp[1] + stairs[1] + stairs[2])
    
    print(dp[-1])