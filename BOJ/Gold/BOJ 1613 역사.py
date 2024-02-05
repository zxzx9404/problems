# PyPy3로만 통과

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x : int(x)-1, input().split())
    arr[a][b] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

S = int(input())
for _ in range(S):
    a, b = map(lambda x : int(x)-1, input().split())
    if arr[a][b]:
        print(-1)
    elif arr[b][a]:
        print(1)
    else:
        print(0)
