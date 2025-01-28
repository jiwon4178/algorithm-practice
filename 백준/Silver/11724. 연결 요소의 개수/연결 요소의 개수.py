import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [0] * (N + 1)
for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1 

print(cnt)