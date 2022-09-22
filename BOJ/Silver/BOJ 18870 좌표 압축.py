# 실행 시간 : PyPy : 1132ms / Python : 시간 초과

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [0]*n
arr2 = sorted(list(set(arr)))

for i in range(n):
    left, right = 0, len(arr2)-1
    while left <= right:
        mid = (left + right) // 2
        if arr2[mid] > arr[i]:
            right = mid - 1
        elif arr2[mid] < arr[i]:
            left = mid + 1
        else:
            ans[i] = mid
            break
print(*ans)


# 인터넷에서 본 풀이 // dict를 이용한다.
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')
'''