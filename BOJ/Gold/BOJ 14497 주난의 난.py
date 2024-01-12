from collections import deque
import sys
input = sys.stdin.readline

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
arr = [list(input().strip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dq = deque()
temp = deque()
visited[x1][y1] = 1
dq.append([x1, y1])
cnt = 1

while dq:
    i, j = dq.popleft()
    
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if ni < 0 or ni == N or nj < 0 or nj == M: continue
        if visited[ni][nj]: continue
        visited[ni][nj] = 1
        if arr[ni][nj] == '1':
            temp.append([ni, nj])
        elif ni == x2 and nj == y2:
            print(cnt)
            quit()
        else:
            dq.append([ni, nj])
    
    
    if not dq and temp:
        dq = temp
        temp = deque()
        cnt += 1
   
