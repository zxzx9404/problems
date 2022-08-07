import sys

n = int(input())
list_n = list(map(int, sys.stdin.readline().split()))
m = int(input())
list_m = list(map(int, sys.stdin.readline().split()))


list_n.sort()

for i in list_m:
    left, right = 0, n-1
    find = False
    while left <= right:
        mid = (left+right)//2
        if i == list_n[mid]:
            print(1)
            find = True
            break
        elif i > list_n[mid]:
            left = mid +1
        else:
            right = mid-1
    if find is False:
        print(0)
        
'''
문제의 의도는 이분탐색.
그러나 인풋 데이터의 한계때문인지 set을 활용했을때 속도가 4배나 빠름..;

import sys

n = int(input())
list_n = set(map(int, sys.stdin.readline().split()))
m = int(input())
list_m = list(map(int, sys.stdin.readline().split()))

for i in list_m:
    if i in list_n:
        print('1')
    else:
        print('0')
        
-set을 활용한 코드
'''