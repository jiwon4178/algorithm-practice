N, L = map(int, input().split())

M = [] # map 
for i in range(N):
    M.append(list(map(int, input().split())))

res = 0 # 가능한 길의 개수 


for i in range(N):
    up = 1
    down = 0
    h = M[i][0] # 맨 처음 열이 시작높이 
    for j in range(1,N):
        if M[i][j] == h :
            if down != 0 : # 한칸 아래가 있었다는 의미. 근데 경사로를 못놓기 때문에 break
                break 
            else : # down == 0 -> 내려가는게 없다.
                up += 1 # 경사로 가능 길이 + 1  
               # continue # 계속 옆으로 가면 됨 

        elif M[i][j] == h + 1 : 
            # up += 1
            if up >= L : 
                up = 1
                down = 0 # 높이 바뀌었기 때문에 초기화 
                h = M[i][j]
            else : break 
        elif M[i][j] == h - 1:
            down += 1
            if down >= L: # 경사로 둘수 있는 길이가 되면 
                up = 0
                down = 0
                h = M[i][j] # 내려감 
        else:
            break
    
        if j == N -1 and down == 0 : 
            res += 1 


for j in range(N):
    up = 1
    down = 0
    h = M[0][j] # 맨 처음 행이 시작높이 
    for i in range(1,N):
        if M[i][j] == h :
            if down != 0 : # 한칸 아래가 있었다는 의미. 근데 경사로를 못놓기 때문에 break
                break 
            else : # down == 0 -> 내려가는게 없다.
                up += 1 # 경사로 가능 길이 + 1  

        elif M[i][j] == h + 1 : 
            # up += 1
            if up >= L : 
                up = 1
                down = 0 # 높이 바뀌었기 때문에 초기화 
                h = M[i][j]
            else : break 
        elif M[i][j] == h - 1:
            down += 1
            if down >= L: # 경사로 둘수 있는 길이가 되면 
                up = 0
                down = 0
                h = M[i][j] # 내려감 

        else:
            break
        
        if i == N -1 and down == 0 : 
            res += 1
     
    
                
print(res)
