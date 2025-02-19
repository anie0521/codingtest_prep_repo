import sys

def backtrack(n, m, visited, current):
    if len(current) == m:
        print(" ".join(map(str, current)))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            current.append(i)
            backtrack(n, m, visited, current)
            current.pop()
            visited[i] = False


n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)
current = []

backtrack(n, m, visited, current)