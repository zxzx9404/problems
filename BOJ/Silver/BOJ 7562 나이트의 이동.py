from heapq import heappop, heappush

di = [-1, -2, -2, -1, 1, 2, 2, 1]
dj = [-2, -1, 1, 2, 2, 1, -1, -2]

TC = int(input())

for _ in range(TC):
    N = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    visited = [[10**8]*N for _ in range(N)]
    
    hq = []
    visited[si][sj] = 0
    heappush(hq, (0, si, sj))
    
    while hq:
        cnt, i, j = heappop(hq)
                
        if cnt > visited[i][j]: continue
        if i == ei and j == ej:
            break
        
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > visited[i][j] + 1:
                visited[ni][nj] = visited[i][j] + 1
                hq.append((cnt+1, ni, nj))

    print(visited[ei][ej])
