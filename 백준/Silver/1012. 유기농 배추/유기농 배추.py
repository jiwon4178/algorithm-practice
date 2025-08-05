## dfs 
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, M, N):

    # 현재 좌표 연결된 다른 좌표 재귀 방문 
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if (0 <= x1 < M ) and (0 <= y1 < N ): # 범위내 + 배추 있으면 
            if graph[x1][y1] == 1:
                graph[x1][y1] = 0 # 방문
                dfs(x1,y1, M, N)


T = int(input()) 
for i in range(T):
    answer = 0
    M, N, K = map(int, input().split()) # 가로, 세로, 총 배추 개수 
    # 배추 인접 행렬 그래프 
    graph = [[0] * N for _ in range(M)] # M X N (가로 X 세로 길이)
    answer = 0 

		# 배추 위치 표시 
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    # 전체 순회 
    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                answer += 1
                dfs(x,y,M, N)
    
    print(answer)