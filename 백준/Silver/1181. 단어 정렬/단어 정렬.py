N = int(input())

arr = []
for i in range(N):
    arr.append(input())

arr = list(set(arr)) # 중복 제거 
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)