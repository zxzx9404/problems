from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def dijk(st):
    hq = []
    visited[st][0] = 0
    heapq.heappush(hq, [0, st])
    while hq:
        sum_cost, now = heapq.heappop(hq)
        
        # if visited[now] < sum_cost: continue
        
        for next, cost in nodes[now]:
            new_cost = sum_cost + cost

            if visited[next][K-1] > new_cost:
                visited[next][K-1] = new_cost
                visited[next].sort()
                heapq.heappush(hq, [new_cost, next])


N, M, K = map(int, input().split())
nodes = defaultdict(list)
visited = [[int(1e9)]*K for _ in range(N+1)]

for _ in range(M):
    a, b, s = map(int, input().split())
    nodes[a].append([b, s])

dijk(1)
# print(visited[1:])
for i in visited[1:]:
    if i[K-1] == int(1e9):
        print(-1)
    else:
        print(i[K-1])
