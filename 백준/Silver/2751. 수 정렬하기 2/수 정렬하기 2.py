import sys 

# 기본 내장함수로 풀기 

N = int(input())

array = []
for i in range(N):
    array.append(int(sys.stdin.readline()))

array.sort() # or # sorted(array) 사용 

for i in range(N):
    print(array[i])