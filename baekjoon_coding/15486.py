import sys

n = int(sys.stdin.readline())

work_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (n  + 1)

for i in range(n - 1, -1, -1):
    time, money = work_list[i]
    end_day = i + time

    if end_day <= n:
        dp[i] = max(dp[i + 1], dp[end_day] + money)
    else:
        dp[i] = dp[i + 1]

print(dp[0])