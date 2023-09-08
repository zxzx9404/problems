from collections import deque

N, M = map(int, input().split())
sw, sh, ew, eh = map(int, input().split())
sw -= 1; sh -= 1; ew -= 1; eh -= 1

maze = [list(map(int, input())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

ans = -1
arr = deque([[sh, sw]])

while arr:
    i, j = arr.popleft()
    
    for k in range(4):
        ni, nj = i + dy[k], j + dx[k]
        
        if ni >= 0 and ni < M and nj >= 0 and nj < N and not maze[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = visited[i][j] + 1
            arr.append([ni, nj])

for kk in visited:
    print(kk)
print(visited[eh][ew])

'''
10 6
1 3 9 4
0000001000
0111100010
0100010100
0101010100
0101010110
0001000000
'''
