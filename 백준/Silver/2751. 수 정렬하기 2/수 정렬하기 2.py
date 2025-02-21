import sys

def merge(arr, low, high):
    temp = []
    mid = (low + high) // 2
    i, j = low, mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    for k in range(low, high + 1):
        arr[k] = temp[k - low]

    return arr

def merge_sort(arr, low, high):
    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    merge(arr, low, high)

# 입력 받기
N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 병합 정렬 실행
merge_sort(arr, 0, N - 1)

# 정렬된 결과 출력
for num in arr:
    print(num)
