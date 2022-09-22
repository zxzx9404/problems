# 시작점이 여러개인 bfs 탐색 방식

from collections import deque

# dfs 함수
def dfs(N, M):
    q = deque()
    # 정답은 최소 1칸이기 때문에 1로 가정
    max = 1
    # 시작점 찾아서 visited 리스트 값 설정해주고, 큐에 넣어주기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                visited[i][j] = 1
                q.append((i, j))
                
    # 8방향 델타 탐색
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                # max값 탐색
                if max < visited[ni][nj]:
                    max = visited[ni][nj]
    return max


N, M = map(int, input().split())
arr = [input().split() for _ in range(N)]

visited = [[0]* M for _ in range(N)]

# 시작점을 1로 가정해서 풀었으므로 정답은 max값-1
print(dfs(N, M)-1)
