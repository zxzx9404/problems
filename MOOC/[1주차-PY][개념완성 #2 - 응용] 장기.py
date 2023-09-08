from collections import deque

N, M = map(int, input().split())
R, C, S, K = [int(x) - 1 for x in input().split()]

visited = [[0]*M for _ in range(N)]
visited[R][C] = 1

deq = deque([[R, C]])
di = [-2, -2, -1, 1, 2, 2, 1, -1]
dj = [-1, 1, 2, 2, 1, -1, -2, -2]

while deq:
    i, j = deq.popleft()
    
    for k in range(8):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = visited[i][j] + 1
            deq.append([ni, nj])

print(visited[S][K] - 1)
