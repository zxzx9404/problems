def bfs(i, j):
    global cnt
    # 재귀구조로 호출시마다 카운트를 +1
    cnt += 1
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == arr[i][j] + 1:
            bfs(ni, nj)


TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    temp_max = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            bfs(i, j)
            # 더 긴 경로를 발견했거나, 같은 경로에서 시작 숫자가 더 작을 경우
            if temp_max < cnt or (arr[i][j] < ans and temp_max == cnt):
                temp_max = cnt
                ans = arr[i][j]
                
    print(f'#{tc} {ans} {temp_max}')