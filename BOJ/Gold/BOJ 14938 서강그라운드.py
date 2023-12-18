from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N, M, E = map(int, input().split())
values = [0] + list(map(int, input().split()))
nodes = defaultdict(list)

for _ in range(E):
    u, v, c = map(int, input().split())
    nodes[u].append([v, c])
    nodes[v].append([u, c])



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
            new_cost = sum_cost + cost
            if visited[next] > new_cost:
                visited[next] = new_cost
                heapq.heappush(hq, [new_cost, next])

    return visited

ans = 0
for i in range(1, N+1):
    vst = dijk(i)
    temp = 0
    for j in range(1, N+1):
        if vst[j] <= M:
            temp += values[j]
    ans = max(ans, temp)
    
print(ans)
