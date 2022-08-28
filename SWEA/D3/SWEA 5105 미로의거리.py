def bfs(i, j, n): # bfs 탐색
    q = [(i, j)]
    visited[i][j] = 1 # 출발점 1로 만듬
    while q:
        y, x = q.pop(0)
        for di, dj in delta: # 델타 활용하여 4방위 체크하기
            ni, nj = y+di, x+dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != '1' and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[y][x] + 1 # 한칸 떨어질때마다 +1



TC = int(input())
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 델타

for tc in range(1, TC+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())

    # 시작점과 도착점의 좌표 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':       
                idx_i, idx_j = i, j
            if arr[i][j] == '3':
                gol_i, gol_j = i, j
    # visited list 만들기   
    visited = [[0]*n for _ in range(n)]
    bfs(idx_i, idx_j, n)
    
    # 도착점의 visited가 0인 경우, 길이 이어지지 않음 (0 출력)
    if visited[gol_i][gol_j] == 0:
        print(f'#{tc} {0}')
    # 길이 있는 경우, 시작점과 도착점을 뺀 값을 출력해야 하므로 -2
    else:
        print(f'#{tc} {visited[gol_i][gol_j]-2}')