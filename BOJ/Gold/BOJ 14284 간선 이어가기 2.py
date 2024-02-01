import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
S, T = map(int, input().split())
visited = [INF]*(N+1)
visited[S] = 0

    
q = []
heappush(q, [0, S])

while q:
    cost, now = heappop(q)
    
    if cost > visited[now]: continue
    
    for next, next_cost in adj[now]:
        nc = cost + next_cost
        if nc < visited[next]:
            visited[next] = nc
            heappush(q, [nc, next])

print(visited[T])
