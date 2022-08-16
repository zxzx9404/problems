from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while queue:
        z, x, y = queue.popleft()
        
        for i in range(6):
            a = z + dz[i]
            b = x + dx[i]
            c = y + dy[i]
            if 0 <= a < h and 0 <= b < n and 0 <= c < m and arr[a][b][c] == 0:
                queue.append([a,b,c])
                arr[a][b][c] = arr[z][x][y]+1


m,n,h = map(int,input().split())
arr = []
queue = deque([])
for k in range(h):
    temp = []
    for i in range(n):
        temp.append(list(map(int,input().split())))
    arr.append(temp)
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1:
                queue.append([k,i,j])


dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

bfs()
ans = 0
for k in arr:
    for i in k:
        for j in i:
            if j==0:
                print(-1)
                exit(0)
        ans = max(ans,max(i))
print(ans-1)

# 3차원 list 및 3차원 델타 다루는 방법 익히는 문제