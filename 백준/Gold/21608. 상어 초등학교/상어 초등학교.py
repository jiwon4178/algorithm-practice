N = int(input())
# student = N**2
S = [] # 학생들 취향 
C = [[0] * N for _ in range(N)] # 교실 

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


for i in range (N**2):
    S.append(list(map(int, input().split())))

for i in range(N**2):
    s_cnt  = [[0] * N for _ in range(N)]
    e_cnt  = [[0] * N for _ in range(N)]


    for r in range(N):
        for c in range(N):
            if C[r][c] == 0 :
                s_tmp, e_tmp = 0,0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N: # 범위내 
                        if C[nr][nc] in S[i][1:] : # 
                            s_tmp += 1 
                        if C[nr][nc] == 0 : 
                            e_tmp += 1
                s_cnt[r][c] = s_tmp
                e_cnt[r][c] = e_tmp 
            else:
                s_cnt[r][c] = -999
                e_cnt[r][c] = -999

    
    max_v = max(map(max,s_cnt)) # 인접학생들 max값 
    M_li = []
    for r in range(N):
        for c in range(N):
            if s_cnt[r][c] == max_v: 
                M_li.append((4 - e_cnt[r][c] , r, c)) # 여러개면 리스트로.. 
    M_li = list(sorted(M_li, key = lambda x:(x[0], x[1], x[2]))) # 오름차순 정렬 
    # 정렬 조건 : 인접한 곳 빈값이 제일 많을때, 행이 작을때, 열이 작을 때 

    if len(M_li) != 0 :
        A, x, y = M_li[0]

    C[x][y] = S[i][0] # i번째 학생이 앉음 



# 만족도 계산하기 

res = 0

for i in range(N**2):
    for r in range(N):
        find = False
        for c in range(N):
            if S[i][0] == C[r][c]: # 그 학생 찾았으면 만족도 조사 
                s_tmp= 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N: # 범위내 
                        if C[nr][nc] in S[i][1:] : # 
                            s_tmp += 1 
                break 
        if find :
            break 
    
    if s_tmp != 0:
        res += 10**(s_tmp-1)

print(res)