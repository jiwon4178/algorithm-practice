def solution(n, lost, reserve):
    answer = 0
    
    # 정렬 
    lost.sort()
    reserve.sort()
    
    reserve_list = reserve[:]
        
    # 중복제거 
    for i in reserve_list: 
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
    
    for i in reserve:
        if (i - 1) in lost:
            lost.remove(i - 1)
        elif (i + 1) in lost:
            lost.remove(i + 1)
    
    answer = n - len(lost)
    
    
    
    
    return answer