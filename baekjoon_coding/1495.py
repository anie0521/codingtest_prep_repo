import sys

# n -> 연주할 곡의 개수(1 <= n <= 50), s -> 시작 볼륨 (0 <= s <= m)
# m -> 최대 볼륨 (1 <= m <= 1000)

def volume_for_the_last_song(n, s, m):
    n_condition = (1 <= n <= 50)
    s_condition = (0 <= s <= m)
    m_condition = (1 <= m <= 1000)

    if not n_condition or not s_condition or not m_condition:
        return -1
    
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][s] = True

    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:

                if j + volume_list[i] <= m:
                    dp[i + 1][j + volume_list[i]] = True
                
                if j - volume_list[i] >= 0:
                    dp[i + 1][j - volume_list[i]] = True
    
    max_volume = -1

    for v in range(m, -1, -1):
        if dp[n][v]:
            max_volume = v
            break
    
    return max_volume


n, s, m = map(int, sys.stdin.readline().split())

volume_list = list(map(int, sys.stdin.readline().split()))

print(volume_for_the_last_song(n, s, m))
