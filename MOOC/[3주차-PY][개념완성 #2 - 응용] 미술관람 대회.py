def check_RGB(st_i, st_j):
    RGB = [(st_i, st_j)]
        
    while RGB:
        i, j = RGB.pop()
        
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[i][j] == arr[ni][nj]:
                visited[ni][nj] = 1
                RGB.append((ni, nj))

N = int(input())
arr = [list(input()) for _ in range(N)]
ans_RG_B = 0
ans_RGB = 0
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            check_RGB(i, j)
            ans_RGB += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            check_RGB(i, j)
            ans_RG_B += 1

print(ans_RGB, ans_RG_B)
