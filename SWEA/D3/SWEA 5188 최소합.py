def dfs(i, j):
    global ans, temp
    # 방문 처리
    visited[i][j] = 1
    # 해당 좌표값 더해주기
    temp += arr[i][j]
    # 끝점에 도달했다면
    if i == j == n-1:
        # 기존 답과 현재 답중 작은 값을 저장
        ans = min(ans, temp)
        return
    # 이미 현재 답보다 크다면 더이상 탐색 X (가지치기)
    elif temp > ans:
        return
    
    # 좌상 -> 우하로 최단경로에 가야하므로, -1 방향으로는 X
    for di, dj in [[0, 1], [1, 0]]:
        ni, nj = i + di, j + dj
        if ni < n and nj < n and visited[ni][nj] == 0:
            dfs(ni, nj)
            # return 후에 방문 제거해주고, temp에서 값 빼주기
            temp -= arr[ni][nj]
            visited[ni][nj] = 0
    
    
    
    
TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    ans = 1000000
    temp = 0
    dfs(0, 0)
    print(f'#{tc} {ans}')