from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

ans = 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

deq = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            deq.append([i, j])
            
while deq:
    i, j = deq.popleft()
    
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        
        if 0 <= ni < N and 0 <= nj < M and not tomato[ni][nj]:
            tomato[ni][nj] = tomato[i][j] + 1
            deq.append([ni, nj])
            
for i in tomato:
    if 0 in i:
        ans = 0
        break
    ans = max(ans, max(i))

print(ans - 1)
