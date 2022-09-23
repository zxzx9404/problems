def dfs(i, j, dir):
    global ans, temp

    if i < 0 or i == N or j < 0 or j == N:
        return

    if i == sti and j == stj and temp:
        ans = max(ans, len(temp))
        return
    
    if arr[i][j] not in temp:
        temp.append(arr[i][j])
        if dir == 4:
            dfs(i+delta[dir][0], j+delta[dir][1], dir)
        else:
            dfs(i+delta[dir][0], j+delta[dir][1], dir)
            temp.remove(arr[i][j])
            temp.append(arr[i][j])
            dfs(i+delta[dir+1][0], j+delta[dir+1][1], dir+1)
        temp.remove(arr[i][j])


delta = [[], [1, 1], [1, -1], [-1, -1], [-1, 1]]

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(N):
        for j in range(N):
            temp = []
            sti, stj = i, j
            dfs(i, j, 1)

    print(f'#{tc} {ans}')