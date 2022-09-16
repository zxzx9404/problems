import sys
input = sys.stdin.readline

def dfs(i, j, dsum, cnt):
    global maxValue

    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return


    for n in range(4):
        ni = i+delta[n][0]
        nj = j+delta[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:

            visited[ni][nj] = 1
            dfs(ni, nj, dsum + arr[ni][nj], cnt+1)
            visited[ni][nj] = 0

# 광기의 델타 사용법
def u_tetro(i, j):
    global maxValue
    
    for di, dj, dii, djj, diii, djjj in [[0, -1, 1, 0, 0, 1], [-1, 0, 0, -1, 1, 0], [0, -1, -1, 0, 0, 1], [-1, 0, 0, 1, 1, 0]]:
        ni, nj, nii, njj, niii, njjj = i + di, j + dj, i + dii, j + djj, i + diii, j + djjj
        if 0 <= ni < N and 0 <= nj < M and 0 <= nii < N and 0 <= njj < M and 0 <= niii < N and 0 <= njjj < M:
            temp = arr[i][j] + arr[ni][nj] + arr[nii][njj] + arr[niii][njjj]
            maxValue = max(temp, maxValue)


delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


maxValue = 0

for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = 0
        u_tetro(i, j)

print(maxValue)