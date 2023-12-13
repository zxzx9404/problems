from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
nodes = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    nodes[u].append([v, w])
    nodes[v].append([u, w])

v1, v2 = map(int, input().split())

def dijk(st):
    
    visited = [int(1e9)]*(N+1)
    visited[st] = 0
    hq = []
    heapq.heappush(hq, [0, st])

    while hq:
        sum_cost, now = heapq.heappop(hq)
        
        if visited[now] < sum_cost:
            continue
        
        for next, cost in nodes[now]:
            if visited[next] > sum_cost + cost:
                visited[next] = sum_cost + cost
                heapq.heappush(hq, [sum_cost + cost, next])

    return visited


from_1 = dijk(1)
from_v1 = dijk(v1)
from_v2 = dijk(v2)

v1_sum = from_1[v1] + from_v1[v2] + from_v2[N]
v2_sum = from_1[v2] + from_v2[v1] + from_v1[N]
ans = min(v1_sum, v2_sum)
print(ans if ans < int(1e9) else -1)
