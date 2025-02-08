import sys

N,M = map(int, sys.stdin.readline().split())

map = []

for _ in range(N):
    map.append(input())

max_square = 0
size = 1

while size <= min(N, M):
    for i in range(N - size + 1):
        for j in range(M - size + 1):
            if (map[i][j] == map[i][j + size - 1] and
                map[i][j] == map[i + size - 1][j] and
                map[i][j] == map[i + size - 1][j + size - 1]):
                max_square = max(max_square, size * size)
    
    size += 1

print(max_square)