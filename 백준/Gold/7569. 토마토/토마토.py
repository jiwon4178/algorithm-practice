from collections import deque 
import copy 
M, N, H = map(int, input().split())

tomato = []


for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    tomato.append(tmp)
# h, n, m (h, r, c)

nr = [1,0,0,-1,0,0]
nc = [0,1,0,0,-1,0]
nh = [0,0,1,0,0,-1]

deq = deque([])
for z, d in enumerate(tomato):
    for y, h in enumerate(d):
        for x, w in enumerate(h):
            if w == 1:
                deq.append([z,y,x])

cnt = 0 # 걸리는 날 

def isTo(box):
    for a in box:
        for b in a:
            for c in b:
                if c == 0 :
                    return False # 안익은 토마토가 있다... 
    
    # 안익은 토마토가 없다! 
    return True

while deq:
    if isTo(tomato): # 안익은 토마토가 없다면 
        print(cnt)
        break 
    
    cnt += 1

    deq_ = copy.deepcopy(deq) # 이미 익은 토마토 deq_로
    deq = deque([]) # 오늘 익힌 토마토 

    while deq_:
        z, y, x = deq_.popleft()
        for i in range(6):
            nx = x + nc[i]
            ny = y + nr[i]
            nz = z + nh[i]
            
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = 1
                deq.append([nz, ny, nx])
 
 
# 토마토가 모두 익지 않았으면
if not isTo(tomato):
    print(-1)