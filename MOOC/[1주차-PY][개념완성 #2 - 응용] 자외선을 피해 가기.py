from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[10**8]*N for _ in range(N)]
visited[0][0] = 0
deq = deque([[0, 0]])
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

while deq:
    i, j = deq.popleft()
    
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > visited[i][j] + arr[ni][nj]:
            visited[ni][nj] = visited[i][j] + arr[ni][nj]
            deq.append([ni, nj])

print(visited[N-1][N-1])
