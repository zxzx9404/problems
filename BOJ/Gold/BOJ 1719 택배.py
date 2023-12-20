from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijk(st):
    visited[st] = 0
    FROM = [0]*(N+1)    
    
    hq = []
    heappush(hq, [0, st])
    
    while hq:
        cost, now = heappop(hq)
        
        if visited[now] < cost: continue
        
        for next, c in nodes[now]:
            new_cost = cost + c
            if visited[next] > new_cost:
                visited[next] = new_cost
                FROM[next] = now
                heappush(hq, [new_cost, next])

    ans = [0]*(N+1)

    for i in range(1, N+1):
        if i == st: continue
        now = i
        while True:
            if FROM[now] == st:
                break
            now = FROM[now]
        ans[i] = now
        
    ans[st] = '-'
    print(*ans[1:])

N, M = map(int, input().split())
nodes = defaultdict(list)

for _ in range(M):
    a, b, s = map(int, input().split())
    nodes[a].append([b, s])
    nodes[b].append([a, s])

for i in range(1, N+1):
    visited = [int(1e9)]*(N+1)
    dijk(i)
