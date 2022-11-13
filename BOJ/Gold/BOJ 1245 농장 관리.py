def bfs(i, j):
    q =[(i, j)]
    p = 1
    while q:
        y, x = q.pop()
        for di, dj in delta:
            ni, nj = y + di, x + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] > arr[i][j]:
                    p = 0
                elif arr[i][j] == arr[ni][nj] and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    return p
        
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
ans = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            ans += bfs(i, j)

print(ans)