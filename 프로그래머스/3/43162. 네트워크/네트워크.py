# def dfs(n, computers, start, visited):
#     stack = [start] 
#     while stack:
#         com = stack.pop()
#         visited.append(com)
#         for connect in range(n):
#             if connect != com and computers[com][connect] == 1 and (connect not in visited):
#                 stack.append(connect)



# def solution(n, computers):
#     answer = 0
#     # 리스트 정의 
#     visited = list()
    
    
#     for com in range(n):
#         if com not in visited:
#             dfs(n, computers, com, visited)
#             answer += 1
#     return answer

from collections import deque
def bfs(n, computers, start, visited):
    visited[start] = True # 방문 표시 
    queue = deque([start])
    
    while queue:
        com = queue.popleft()
        if visited[com] != True: # 방문안했으면 
            visited[com] = True # 방문처리하고 
        for connect in range(n):
            if connect != com and computers[com][connect] == 1 and visited[connect] != True:
                queue.append(connect)
        # print(queue)


def solution(n, computers):
    answer = 0
    
    # 방문 노드 정의 
    visited = [False for _ in range(n)]
    
    for com in range(n):
        if visited[com] != True: # 방문 안했으면 
            bfs(n, computers, com, visited)
            answer += 1
    return answer
            
            
            
