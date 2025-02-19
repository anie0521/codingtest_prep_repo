""" 
1번째 입력값 -> 테스트 케이스의 개수 
2번째 입력값 -> m(가로), n(세로), k(배추가 심어져 있는 위치)
3번째 입력값 -> 배추의 위치 x, y
"""

import sys

def count_earthworm_dfs(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 1:
                continue

            cnt += 1
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue
                    if grid[nx][ny] == 1:
                        stack.append((nx, ny))
                        grid[nx][ny] = 0
    return cnt

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    cabbages = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]
    grid = [[0] * m for _ in range(n)]
    for y, x in cabbages:
        grid[x][y] = 1
    print(count_earthworm_dfs(grid))



# m_dict = {}
# n_dict = {}
# k_dict = {}
# cabbages_dict = {}

# for i in range(t):
#     m, n, k = map(int, sys.stdin.readline().split())
#     cabbages = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]

#     m_dict[f"m{i}"] = m
#     n_dict[f"n{i}"] = n
#     k_dict[f"k{i}"] = k
#     cabbages_dict[f"cabbages{i}"] = cabbages