def bfs(i, j, n):
    # 델타
    delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # 큐에 출발점 좌표 입력
    q = [(i, j)]
    # 출발점의 visited를 1로 바꿈
    visited[i][j] = 1
    while q:
        tpi, tpj = q.pop(0)
        for di, dj in delta:
            ni, nj = tpi+di, tpj+dj
            # ni, nj가 미로 범위 안이고, 벽이 아니며, 방문한 적이 없을 경우
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                # ni, nj를 큐에 추가하고 방문으로 바꿈
                q.append((ni, nj))
                visited[ni][nj] = 1


for _ in range(1, 11):
    tc = int(input())
    maze = []
    for _ in range(16):
        maze.append(input())
    # 2차원 visited list 생성
    visited = [[0]*16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            # 시작점 좌표
            if maze[i][j] == '2':
                sti, stj = i, j
            # 목표점 좌표
            if maze[i][j] == '3':
                endi, endj = i, j

    bfs(sti, sti, 16)
    # 시작점에서 목표점에 방문이 가능하면 목표점의 visited 좌표가 1, 아니면 0
    print(f'#{tc} {visited[endi][endj]}')