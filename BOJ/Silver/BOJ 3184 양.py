R, C = map(int, input().split())
arr = [input() for _ in range(R)]
visited = [[0]*C for _ in range(R)]
ans_s, ans_w = 0, 0

for i in range(R):
    for j in range(C):
        if not visited[i][j] and arr[i][j] != '#':
            stk = [(i, j)]
            ship, wolf = 0, 0
            visited[i][j] = 1

            while stk:
                ii, jj = stk.pop()
                if arr[ii][jj] == 'o':
                    ship += 1
                elif arr[ii][jj] == 'v':
                    wolf += 1
                for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                    ni, nj = ii + di, jj + dj
                    if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and arr[ni][nj] != '#':
                        visited[ni][nj] = 1
                        stk.append((ni, nj))

            if ship > wolf:
                ans_s += ship
            else:
                ans_w += wolf

print(ans_s, ans_w)