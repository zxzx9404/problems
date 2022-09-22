'''
접근 아이디어 
1. 시작 시간과 무관하게 끝나는 시간이 가장 빠른 회의를 찾는다.
2. 끝나는 시간이 같다면 그 중 가장 빠른 시작시간을 가진 회의를 pick
3. 2번에서 pick한 회의가 끝나는 시점부터 탐색을 재개하여 다시 1~2 과정을 반복
'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = deque()

max = 0
for _ in range(N):
    arr.append(list(map(int, input().split())))
        

# 끝나는 시간이 먼저 도래하는 순으로 sort          
arr = sorted(arr, key= lambda x : (x[1], x[0]))

# 가장 먼저 끝나는 회의의 종료시간을 현재시간으로
t = arr[0][1]
idx = 1
while idx < len(arr):
    # 만약 다음 회의의 시작시작 혹은 종료시간이 현재시간보다 빠르다면
    if arr[idx][0] < t or arr[idx][1] < t:
        # 가장 많은 회의를 진행하기 위해 필요하지 않은 회의이므로 삭제
        arr.pop(idx)
    else:
        # 아니라면 필요한 회의이므로 그 회의의 종료시간을 t로 바꿈
        t = arr[idx][1]
        idx += 1


print(idx)