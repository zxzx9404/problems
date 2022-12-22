from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
visited[0][0] = 0
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

q = deque([(0, 0)])

while q:
    i, j = q.popleft()
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if visited[ni][nj] == -1:  # 첫 방문
                if arr[ni][nj]:  # 벽일 경우
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
                else:  # 통로일 경우
                    visited[ni][nj] = visited[i][j]
                    q.appendleft((ni, nj))

print(visited[N-1][M-1])