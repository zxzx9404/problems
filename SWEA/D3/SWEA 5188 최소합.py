def dfs(i, j):
    global ans, temp
    # 방문 처리
    visited[i][j] = 1
    # 해당 좌표 값 더해줌
    temp += arr[i][j]
    # 도착점일 경우, 최소값 비교
    if i == j == n-1:
        ans = min(ans, temp)
        return
    # 이미 최소값보다 클 경우 더이상 탐색 X
    elif temp > ans:
        return
    
    # 좌상 -> 우하이므로 -1 방향은 탐색 X
    for di, dj in [[0, 1], [1, 0]]:
        ni, nj = i + di, j + dj
        if ni < n and nj < n and visited[ni][nj] == 0:
            dfs(ni, nj)
            # 한번 재귀식에 들어갔다온 이후로 값 빼주고 방문처리 빼주기
            temp -= arr[ni][nj]
            visited[ni][nj] = 0
    
    
    
    
TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    # 임의의 큰 값으로 ans 설정
    ans = 1000000
    # 임시합
    temp = 0
    # 0, 0 점으로 탐색 시작
    dfs(0, 0)
    print(f'#{tc} {ans}')