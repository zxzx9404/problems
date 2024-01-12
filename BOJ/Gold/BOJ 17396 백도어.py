from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cannot_go = list(map(int, input().split()))
cannot_go[N-1] = 0
adj = [[] for _ in range(N)]
time = [sys.maxsize]*N

for _ in range(M):
    a, b, t = map(int, input().split())
    if cannot_go[a] or cannot_go[b]: continue
    adj[a].append([b, t])
    adj[b].append([a, t])

hq = []
ans = -1
heappush(hq, [0, 0])
time[0] = 0

while hq:
    cost, now = heappop(hq)
    
    if cost > time[now]: continue
    if now == N-1:
        ans = cost
        break
    
    for next, t in adj[now]:
        next_cost = cost + t
        if time[next] > next_cost:
            time[next] = next_cost
            heappush(hq, [next_cost, next])
            
print(ans)
