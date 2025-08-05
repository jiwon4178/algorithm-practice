N = int(input())
L = int(input())

cnt=0
def dfs(virus):
    global cnt
    visited[virus]=1

    for i in network[virus]:
        if (visited[i]==0):
            dfs(i)
            cnt+=1

def bfs(virus):
    global cnt
    visited[virus] = 1
    queue = [virus]
    while queue:
        for i in network[queue.pop()]:
            if (visited[i]==0):
                visited[i]=1
                queue.insert(0, i)
                cnt+=1


network = [[]*(N+1) for _ in range(N+1)]

for i in range(L):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [0]*(N+1)
bfs(1)
#dfs(1)
print(cnt)