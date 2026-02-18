from collections import deque 
# 노드 및 간선 개수 입력 
n,m = map(int, input().split())

# 그래프 초기화 / 노드 1부터 시작 ... 
graph = [[] for i in range(n+1)]

# 진입차수 초기화 / 모두 0 
indegree = [0] * (n + 1)


# A -> B 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입 차수 추가 
    indegree[b] += 1 


# 위상정렬 함수 
def topology_sort():
    result = [] # 결과 리스트 
    q = deque() # 큐 
    
    # 진입차수 0인 노드 큐에 삽입 
    for i in range(1, n +1):  
        if indegree[i] == 0:
            q.append(i) 

    while q: # 큐가 빌때까지 
        now = q.popleft() # 마지막 
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기 
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    # result.reverse()
    for k in result: 
        print(k, end = " ")

topology_sort()

