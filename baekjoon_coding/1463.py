import sys

def make_one(n):
    min_cnt = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            min_cnt += 1
        elif n % 3 == 0:
            n = n // 3
            min_cnt += 1
        else:
            n -= 1
            min_cnt += 1
    return min_cnt

def make_one_dp(n):
    limit = 1000000
    if n < 1 or n > limit:
        return
    dp = [0] * (n+1)

    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

    return dp[n]

n = int(sys.stdin.readline())

print(make_one_dp(n))
