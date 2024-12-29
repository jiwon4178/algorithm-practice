from collections import deque 

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)] # 위치 

def bfs():
    dx = [-1, -1, -1, 0 , 0, 1, 1, 1] # 방향 8개 
    dy = [-1,  0,  1, -1, 1, 1, 0,-1]
    
    queue = deque() 
    # 아기상어 위치 저장 
    for i in range (N):
        for j in range (M):
            if maps[i][j] == 1:
                queue.append((i,j))
    ans = 0 
    while queue:
        cur_x, cur_y = queue.popleft() # 큐에서 하나 빼기 
        for i in range(8):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if (0 <= next_x < N) and (0 <= next_y < M):  # 범위내 
                if maps[next_x][next_y] == 0: # 아기상어 없음
                    queue.append((next_x, next_y))
                    maps[next_x][next_y] = maps[cur_x][cur_y] + 1
                    ans = maps[next_x][next_y]    

    return ans -1


print(bfs())
