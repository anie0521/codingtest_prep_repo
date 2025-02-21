from collections import deque
import sys


def bfs(n, k):
    visited = [False] * 100001
    q = deque([(n, 0)])
    visited[n] = True

    while q:
        x, t = q.popleft()
        if x == k:
            return t
        
        for next_x in (x + 1, x - 1, 2 * x):
            if 0 <= next_x <= 100000 and not visited[next_x]:
                visited[next_x] = True
                q.append((next_x, t + 1))
        
        
n, k = map(int, sys.stdin.readline().split())

print(bfs(n, k))