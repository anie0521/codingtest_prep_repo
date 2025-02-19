"""
1은 집이 있는곳 0은 집이 없는곳을 나타냄
지도를 입력하여 단지수를 출력

입력값 : 첫번째줄은 지도의 크기 N 
가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력됨

출력값 : 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
"""

from collections import deque
import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())


maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if maps[x][y] == 0:
        return False
    
    maps[x][y] = 0
    size = 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        size += dfs(x + dx, y + dy)
    
    return size

def bfs(x, y):
    q = deque([(x, y)])

    maps[x][y] = 0
    size = 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append((nx, ny))
                size += 1
    
    return size


apt_sizes = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            apt_size = dfs(i, j)
            apt_size = bfs(i, j)
            apt_sizes.append(apt_size)


apt_sizes.sort()

print(len(apt_sizes))
for size in apt_sizes:
    print(size)