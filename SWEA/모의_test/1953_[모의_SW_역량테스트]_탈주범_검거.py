def bfs(i, j):
    global cnt
    # BFS 방식 사용
    q = [(i, j)]
    while q:
        i, j = q.pop(0)
        # 각각 파이프 모양에 따라 델타 탐색의 방위가 달라짐            
        for di, dj in delta[arr[i][j]]:
            ni, nj = i + di, j + dj
            #      /X축 Y축 모두 범위 안이고/   /방문한 적 없으며/        /빈 칸이 아니며/      /시간 내에 갈 수 있고/        /서로 연결되어 있는 경우/
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] != 0 and visited[i][j] + 1 <= L and [-di, -dj] in delta[arr[ni][nj]]:
                visited[ni][nj] = visited[i][j] + 1
                cnt += 1
                q.append((ni, nj))

TC = int(input())
for tc in range(1, TC+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    # 파이프 모양에 따른 델타 방위
    delta = [
        [],
        [[0, 1], [0, -1], [1, 0], [-1, 0]],
        [[1, 0], [-1, 0]],
        [[0, -1], [0, 1]],
        [[-1, 0], [0, 1]],
        [[1, 0], [0, 1]],
        [[1, 0], [0, -1]],
        [[-1, 0], [0, -1]]
    ]
    
    cnt = 1
    visited[R][C] = 1
    bfs(R, C)
    print(f'#{tc} {cnt}')
    