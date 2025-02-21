import sys

def dfs(x, y):
    maps[y][x] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
            dfs(nx, ny)


t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    cabbages = []

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        cabbages.append((x, y))
    
    maps = [[0] * m for _ in range(n)]

    for x, y in cabbages:
        maps[y][x] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                dfs(j, i)
                cnt += 1
    print(cnt)

dfs(x, y)