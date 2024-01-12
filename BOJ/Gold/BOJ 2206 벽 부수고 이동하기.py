# 벽을 부순 visited, 벽을 부수지 않은 visited를 각각 만들어야 함 -> 3차원 visited 필요

from collections import deque
import sys

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def bfs():
    visited = [[[sys.maxsize]*2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    
    while q:
        i, j, c = q.popleft()
        
        if i == N - 1 and j == M - 1:
            return visited[i][j][c]
        
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if not arr[ni][nj] and visited[ni][nj][c] > visited[i][j][c] + 1:
                    visited[ni][nj][c] = visited[i][j][c] + 1
                    q.append((ni, nj, c))
                if arr[ni][nj] and not c:
                    visited[ni][nj][1] = visited[i][j][0] + 1
                    q.append((ni, nj, 1))
    
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = bfs()
print(ans)
