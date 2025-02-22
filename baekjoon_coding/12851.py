""" 
숨바꼭질 2

bfs -> 큐?
"""
import sys
from collections import deque

def bfs(n, k):
    max_dist = 100000
    visited = [-1] * (max_dist + 1)

    q = deque([(n, 0)])
    visited[n] = 0
    cnt = 0
    min_time = -1


    while q:
        x, time = q.popleft()

        if x == k:
            if min_time == -1:
                min_time = time
                cnt = 1

            elif time == min_time:
                cnt += 1
            
            else:
                break
            
            continue

        for next_x in (x-1, x+1, 2*x):
            if 0 <= next_x <= max_dist:
                if visited[next_x] == -1 or visited[next_x] == time + 1:
                    visited[next_x] = time + 1
                    q.append((next_x, time + 1))

    return min_time, cnt

n, k = map(int, sys.stdin.readline().split())
time, count = bfs(n, k)
print(time)
print(count)