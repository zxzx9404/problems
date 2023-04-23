from collections import deque

def bfs(y, x, year):
    q = deque([(y, x)])
    del_list = []

    while q:
        i, j = q.popleft()
        sea = 0
        
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            
            if not arr[ni][nj]:
                sea += 1
            elif visited[ni][nj] != year:
                q.append((ni, nj))
                visited[ni][nj] = year
            
        if sea:
            del_list.append((i, j, sea))

    for y, x, sea in del_list:
        if arr[y][x] > sea:
            arr[y][x] -= sea
        else:
            arr[y][x] = 0
            glacier.remove((y, x))

    return 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
year = 0
glacier = set()
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            glacier.add((i, j))
            
while glacier:
    year += 1    
    group = 0
    
    for i, j in list(glacier):
        if arr[i][j] and visited[i][j] != year:
            visited[i][j] = year
            group += bfs(i, j, year)
    
    if group > 1:
        print(year-1)
        break

if group < 2:
    print(0)