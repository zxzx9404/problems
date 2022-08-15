# BFS를 사용 (미사용시 시간초과)

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and arr[a][b] == 0:
                queue.append([a,b])
                arr[a][b] = arr[x][y]+1


m,n = map(int,input().split())
arr = []
queue = deque([])
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(m):
        if arr[i][j]==1:
            queue.append([i,j])
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()
ans = 0
for i in arr:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    ans = max(ans,max(i))
print(ans-1)


# BFS 사용하지 않은 시간초과 버전

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[-1]*(N+2)]

for k in range(1, M+1):
    a = list(map(int, input().split()))
    arr.append(a)
    arr[k].insert(0, -1)
    arr[k].append(-1)
arr.append([-1]*(N+2))



p = True
count = 0
while True:
    su = 0
    count += 1
    for i in range(1, M+1):
        if p == False:
            break
        for j in range(1, N+1):
            if arr[i][j] == 0:
                if arr[i+1][j] == -1 and arr[i-1][j] == -1 and arr[i][j+1] == -1 and arr[i][j-1] == -1:
                    print(-1)
                    p = False
                    break
                elif arr[i+1][j] == count or arr[i-1][j] == count or arr[i][j+1] == count or arr[i][j-1] == count:
                    arr[i][j] = count+1
                else:
                    su += 1
    if p == False:
        break
    elif su == 0:
        break

if p:
    print(count)