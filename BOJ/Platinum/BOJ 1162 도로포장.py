from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
route = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    route[a].append([b, c])
    route[b].append([a, c])

visited = [[sys.maxsize]*(K+1) for _ in range(N+1)]

def dijk(st):
    hq = []
    heapq.heappush(hq, [0, 0, st])
    visited[st][0] = 0
    
    while hq:
        cost, cnt, now = heapq.heappop(hq)
        
        if visited[now][cnt] < cost: continue
        
        if now == N:
            return cost
        
        for next, c in route[now]:
            next_cost = cost + c
            if visited[next][cnt] > next_cost:
                visited[next][cnt] = next_cost
                heapq.heappush(hq, [next_cost, cnt, next])
            
            if cnt + 1 <= K and visited[next][cnt+1] > cost:
                visited[next][cnt+1] = cost
                heapq.heappush(hq, [cost, cnt + 1, next])

ans = dijk(1)
print(ans)
