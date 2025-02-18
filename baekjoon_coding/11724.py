import sys

# 정점의 개수, 간선의 개수
n, m = map(int, sys.stdin.readline().split())

# 노드들을 담기위한 그래프 변수
graph = [[] for _ in range(n+1)]

# 방문한 노드를 저장하는 변수
visited = set([])

# 입력값 갖고 무방향 그래프 만들기
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs
def dfs(node):
    visited.add(node)
    for adj in graph[node]:
        if adj not in visited:
            dfs(adj)

cnt = 0
for node in range(1, n + 1):
    if node not in visited:
        dfs(node)
        cnt += 1


print(cnt)