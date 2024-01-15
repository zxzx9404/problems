from heapq import heappop, heappush
import sys

def find_route(n):
    global flag
    if flag: return
    if FROM[n] == 1: return
    if n == P:
        flag = True
        return
    for i in FROM[n]:
        find_route(i)
    
    
V, E, P = map(int, input().split())
FROM = [set() for _ in range(V+1)]
visited = [sys.maxsize]*(V+1)
adj = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

hq = []
heappush(hq, (0, 1))
visited[1] = 0

while hq:
    cost, now = heappop(hq)
    
    if cost > visited[now]: continue
    
    for next, nc in adj[now]:
        next_cost = cost + nc
        if visited[next] > next_cost:
            FROM[next] = {now}
            visited[next] = next_cost
            heappush(hq, (next_cost, next))
        elif visited[next] == next_cost:
            FROM[next].add(now)
            heappush(hq, (next_cost, next))

flag = False
find_route(V)
if flag:
    print("SAVE HIM")
else:
    print("GOOD BYE")
