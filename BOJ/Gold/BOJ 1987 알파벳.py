def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in arr:
            arr.add(maps[nx][ny])
            dfs(nx, ny, count+1)
            arr.remove(maps[nx][ny])
            
## pypy로만 통과

r, c = map(int, input().split())
maps = [input() for _ in range(r)]
ans = 0
arr = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr.add(maps[0][0])
dfs(0, 0, 1)
print(ans)