# 퀵 정렬 알고리즘
def partition(l, r):
    pivot = arr[l]
    i, j, = l, r
    while i <= j :
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quicksort(l, r):
    if l < r:
        s = partition(l, r)
        quicksort(l, s-1)
        quicksort(s+1, r)
        
        

TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quicksort(0, n-1)
    print(f'#{tc} {arr[n//2]}')