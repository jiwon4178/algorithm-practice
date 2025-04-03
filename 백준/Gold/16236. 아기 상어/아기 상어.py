from collections import deque 
# 리스트 대신 튜플 사용시 좋은점 -> 불변성! 

N = int(input())

s_graph = [] 
for i in range(N):
    s_graph.append(list(map(int,input().split())))

shark = () # 상어 
for i in range(N):
    for j in range(N):
        if s_graph[i][j] == 9 : 
            shark = (i, j) # 상어 위치 


# 1번 돌때마다 먹을 수 있는지 없는지 판단해야함 
# 여기서 visited는 방문여부도 맞는데, 해당 칸까지의 거리도 포함하고 있음 
# 0이면 방문 안 한 곳, 1 이상이면 방문한 곳 + 도달 시간
def bfs(x, y): # 할때마다 visited 초기화해야 한번 쫙 돌게됨 
    visited = [[0] * N for _ in range(N)] # N x N 
    q = deque()
    visited[x][y] = 1 # 시작위치...  
    q.append((x, y)) # or q = deque([(x,y)])

    prey = [] # 먹을 수 있는 경우를 저장 # (거리 , 행(row), 열(col))


    while q: # 돌수 있는 곳은 다 돌아보자 
        i, j = q.popleft() # 안빼면 계속돎 

        for k in range(4): # 4방향 
            nx = i + dr[k]
            ny = j + dc[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 :# 범위내 + 방문 X
                # 먹을 수 있는 경우 - 다음 좌표위치에 있는 물고기 크기가 상어보다 작고, 좌표가 비어있지 않을때 
                if s_graph[nx][ny] < s_graph[x][y] and s_graph[nx][ny] != 0:
                    visited[nx][ny] = visited[i][j] + 1 # 현재위치에서 먹이 있는 위치로 넘어갈때 
                    prey.append((visited[nx][ny]-1, nx, ny)) # default 시작점이 1이였으니까, 움직인 거리는 -1 
                elif s_graph[nx][ny] == s_graph[x][y]: # 못먹고 지나갈 수만 있음 # 큰곳은 지나갈수도 없음; 
                    visited[nx][ny] = visited[i][j] + 1 # 현재 위치 + 1
                    q.append((nx, ny))
                elif s_graph[nx][ny] == 0 : # 빈칸 
                    visited[nx][ny] = visited[i][j] + 1  # 현재 위치 + 1
                    q.append((nx, ny))

    return list(sorted(prey, key=lambda x: (x[0], x[1], x[2]))) # 거리 , 행, 열 순서대로 정렬 진행 

 
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

size = 2 # 상어 크기 
eat = 0 
time = 0 

while True: 
    r, c = shark # 상어위치 
    s_graph[r][c] = size # 사이즈   

    prey = list(bfs(r,c)) # 상어 위치가 r, c일때 먹을 수 있는 list 받아옴 
    if not prey: # prey 없는경우에? while 문 반복 멈춤 
        break 

    # 만약 먹이가 있으면 
    sec, nr, nc = prey[0] # 가장 가까운 먹이 
    # print(prey[0])

    time += sec 
    eat += 1 # 하나 먹음 

    if eat == size : # 크기만큼 먹어야 다음 사이즈가 됨 
        size += 1
        eat = 0 # 초기화 

    s_graph[r][c] = 0 # 위치 옮겼으니까 ? 
    shark = (nr, nc) # 여기로 상어 위치 옮김 


print(time)



