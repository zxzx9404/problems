from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 0
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] > visited[i][j] + arr[ni][nj]:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
                    q.append((ni, nj))
 
T = int(input())
 
for tc in range(1, T+1):
    n = int(input())

    arr = [list(map(int, input())) for _ in range(n)]
    
    # 기존 거리까지의 누적합이 더 작을 경우 바꿔줘야 하므로,
    # 임의의 매우 큰 값으로 visited의 초기값을 설정
    visited = [[100000000000000] * n for _ in range(n)]
 
    bfs(0, 0)
    print(f'#{tc} {visited[n-1][n-1]}')