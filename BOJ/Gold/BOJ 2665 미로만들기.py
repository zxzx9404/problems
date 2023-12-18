import heapq
import sys
# input = sys.stdin.readline

N = int(input())

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
arr = [list(map(int, input())) for _ in range(N)]


def dijk(si, sj):
    visited = [[int(1e9)] * N for _ in range(N)]
    visited[si][sj] = 0
    hq = []
    heapq.heappush(hq, [0, si, sj])

    while hq:
        sum_cost, i, j = heapq.heappop(hq)
        
        if i == N-1 and j == N-1:
            return sum_cost
        
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if (0 > ni or ni == N or 0 > nj or nj == N): continue
            if visited[ni][nj] != int(1e9): continue
            if arr[ni][nj]:
                heapq.heappush(hq, [sum_cost, ni, nj])
                visited[ni][nj] = visited[i][j]
            else:
                heapq.heappush(hq, [sum_cost+1, ni, nj])
                visited[ni][nj] = visited[i][j] + 1

ans = dijk(0, 0)
print(ans)
