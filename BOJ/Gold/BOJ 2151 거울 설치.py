from collections import deque
N = int(input())
visited = [[[10000]*4 for _ in range(N)] for _ in range(N)]

arr = [list(input()) for _ in range(N)]
flag = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == '#':
            if flag:
                end = [i, j]
            else:
                start = [i, j]
                flag = True

q = deque()
for i in range(4):
    visited[start[0]][start[1]][i] = 0
    q.append((start[0], start[1], i))

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

while q:
    i, j, dir = q.popleft()
    
    if arr[i][j] == '!':
        for new_dir in ((dir+1)%4, (dir+3)%4):
            ni, nj = i + di[new_dir], j + dj[new_dir]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '*' and visited[ni][nj][new_dir] > visited[i][j][dir] + 1:
                visited[ni][nj][new_dir] = visited[i][j][dir] + 1
                q.append((ni, nj, new_dir))
        
    
    ni, nj = i + di[dir], j + dj[dir]
    if 0 <= ni < N and 0 <= nj < N:
        if arr[ni][nj] == '*': continue
        
        if visited[ni][nj][dir] > visited[i][j][dir]:
            visited[ni][nj][dir] = visited[i][j][dir]
            q.append((ni, nj, dir))


print(min(visited[end[0]][end[1]]))
