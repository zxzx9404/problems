from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
visited_back = [10**8]*(N+1)
visited_go = [0]*(N+1)
nodes = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    nodes[u].append([v, w])

visited_back[X] = 0
visited_back[0] = 0
hq = []
heapq.heapify(hq)
hq.append([0, X])

while hq:
    sum_cost, now = heapq.heappop(hq)
        
    for next, cost in nodes[now]:
        if visited_back[next] > sum_cost + cost:
            visited_back[next] = sum_cost + cost
            heapq.heappush(hq, [sum_cost + cost, next])


for i in range(1, N+1):
    if i == X: continue
    visited = [10**8]*(N+1)
    visited[i] = 0
    hq = []
    heapq.heapify(hq)
    hq.append([0, i])
    
    while hq:
        sum_cost, now = heapq.heappop(hq)
            
        for next, cost in nodes[now]:
            if visited[next] > sum_cost + cost:
                visited[next] = sum_cost + cost
                heapq.heappush(hq, [sum_cost + cost, next])
    
    visited_go[i] = visited[X]

ans = 0
for a, b in zip(visited_go, visited_back):
    ans = max(ans, a+b)
print(ans)
