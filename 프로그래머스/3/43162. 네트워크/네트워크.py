def dfs(n, computers, start, visited):
    stack = [start] # 이러면 뭐가되는거임...?
    while stack:
        com = stack.pop()
        if com not in visited:
            visited.append(com)
            for connect in range(n):
                if connect != com and computers[com][connect] == 1 and (connect not in visited):
                    stack.append(connect)



def solution(n, computers):
    answer = 0
    
    # 리스트 정의 
    visited = list()
    
    
    for com in range(n):
        if com not in visited:
            dfs(n, computers, com, visited)
            answer += 1
    return answer
            
            
            
        
        
    to_visit.append(0)
    
    while to_visit: 
        node = to_visit.pop()
        
        if node not in visited:
            visited.append(node)
            to_visit.extend(computers[node])
    
    
    return answer