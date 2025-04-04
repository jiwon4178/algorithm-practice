### 시뮬레이션처럼 풀어보기 


def time_after():
    air_cnt = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if air_tmp[i][j] != 0:
                cnt_num = 0
                tmp_num = int(air_tmp[i][j]/5)

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and air_tmp[nx][ny] != -1:
                        air_cnt[nx][ny] += tmp_num 
                        cnt_num += 1
                
                air_cnt[i][j] -= tmp_num * cnt_num
                
    for i in range(R):
        for j in range(C):
            air_tmp[i][j] += air_cnt[i][j]
    
    # for i in range(R):
    #     print(air_tmp[i])


    # 공청기 작동
    for i in range(puri[0]-1,0,-1):
        air_tmp[i][0] = air_tmp[i - 1][0]
    for j in range(C-1):
        air_tmp[0][j] = air_tmp[0][j+1]
    for i in range(puri[0]):
        air_tmp[i][C-1] = air_tmp[i+1][C-1]
    for j in range(C-1, 0, -1):
        air_tmp[puri[0]][j] = air_tmp[puri[0]][j - 1]
    

    for i in range(puri[1]+1,R-1):
        air_tmp[i][0] = air_tmp[i+1][0]
    for j in range(C-1):
        air_tmp[R-1][j] = air_tmp[R-1][j+1]
    for i in range(R-1,puri[1],-1):
        air_tmp[i][C-1] = air_tmp[i - 1][C-1] 
    for j in range(C-1, 0, -1):
        air_tmp[puri[1]][j] = air_tmp[puri[1]][j - 1]
    
    air_tmp[puri[0]][1], air_tmp[puri[1]][1] = 0,0

    # for i in range(R):
    #     print(air_tmp[i])



R, C, T = map(int,input().split())
puri = 0

air_tmp = []
for i in range(R):
    air_tmp.append(list(map(int, input().split())))

puri = []
# 공청기 위치 
for i in range(R):
    if air_tmp[i][0] == -1:
        puri.append(i)

dx = [-1,1,0,0]
dy = [0,0,-1,1]


while T > 0:
    time_after()
    T -= 1 

# for i in range(R):
#     print(air_tmp[i])

answer = sum(map(sum, air_tmp))
answer += 2


print(answer)

