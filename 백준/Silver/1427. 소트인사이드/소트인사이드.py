N = int(input())

arr = []
for i in str(N):
    arr.append(int(i))

arr.sort(reverse=True) # 내림차순

for i in arr:
    print(i,end="") # 공백없이 출력 