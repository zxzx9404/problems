from heapq import heappush, heappop

cnt = 1
while True:
    N = int(input())
    if not N:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    cost = [[10**10]*N for _ in range(N)]
    cost[0][0] = arr[0][0]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []

    
    heappush(q, (0, 0, 0))
    
    while q:
        now, i, j = heappop(q)
    
        for k in range(4):
            ni, nj = i + dy[k], j + dx[k]
            
            if 0 <= ni < N and 0 <= nj < N and cost[i][j] + arr[ni][nj] < cost[ni][nj]:
                cost[ni][nj] = cost[i][j] + arr[ni][nj]
                heappush(q, (cost[ni][nj], ni, nj))

    print(f'Problem {cnt}: {cost[N-1][N-1]}')
    cnt += 1