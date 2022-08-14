# 시간초과 풀이(PyPy3 으로는 가능)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(input().rstrip())

for i in range(M):
    a = input().rstrip()
    if a.isdigit():
        a = int(a)
        print(arr[a-1])
    else:
        print(arr.index(a)+1)
        
        
# 정답 풀이

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = dict()
for k in range(N):
    a = input().rstrip()
    dict[k] = a
    dict[a] = k

for i in range(M):
    a = input().rstrip()
    if a.isdigit():
        a = int(a)
        print(dict[a-1])
    else:
        print(dict[a]+1)