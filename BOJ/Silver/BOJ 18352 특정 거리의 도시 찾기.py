from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N, E, K, X = map(int, input().split())
nodes = defaultdict(list)

for _ in range(E):
    u, v = map(int, input().split())
    nodes[u].append(v)


visited = [int(1e9)]*(N+1)

def dijk(st):    
    visited[st] = 0
    hq = []
    heapq.heappush(hq, [0, st])

    while hq:
        sum_cost, now = heapq.heappop(hq)
        
        if visited[now] < sum_cost:
            continue
        
        for next in nodes[now]:
            if visited[next] > sum_cost + 1:
                visited[next] = sum_cost + 1
                heapq.heappush(hq, [sum_cost + 1, next])

    return visited

dijk(X)
flag = False

for i in range(1, N+1):
    if visited[i] == K:
        flag = True
        print(i)

if not flag:
    print(-1)
