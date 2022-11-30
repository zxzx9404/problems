def dfs(i, j):
    visited[i][j] = 1
    cnt = 1
    stk = [(i, j)]
    
    while stk:
        i, j = stk.pop()
        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj]:
                visited[ni][nj] = 1
                stk.append((ni, nj))
                cnt += 1        
    
    return cnt

N, M, K = map(int, input().split())

arr = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for _ in range(K):
    i, j = map(int, input().split())
    i -= 1; j -= 1
    arr[i][j] = 1

ans = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j]:
            ans = max(ans, dfs(i, j))

print(ans)