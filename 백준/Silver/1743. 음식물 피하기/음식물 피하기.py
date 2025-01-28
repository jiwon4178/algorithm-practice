import sys
sys.setrecursionlimit(100000)

N, M, K = map(int, input().split()) # N = 세로길이(행), M = 가로길이(열), K = 음식물 쓰레기 개수 

graph = [[0]*M for _ in range(N)] # M by N 
visited = [[0]*M for _ in range(N)] # 방문여부 


for _ in range(K):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1 # 쓰레기 위치 표시 

# 상하좌우 방향 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

res = 0

def dfs(graph, visited, x, y):
    global cnt 
    
    visited[x][y] = 1 # 방문여부 표시 

    for i in range (4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny]:
            # print(f'nx = {nx}')
            # print(f'ny = {ny}')
            # print(f'graph[nx][ny] = {graph[nx][ny]}')
            cnt += 1 
            dfs(graph, visited, nx, ny) # 이렇게하면 연결된 곳 모두 돌게됨 


for i in range(N):
    for j in range (M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            dfs(graph, visited, i, j)
            res = max(res, cnt)

print(res)







