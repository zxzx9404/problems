from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
route = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    route[a].append([b, c])
    route[b].append([a, c])

visited = [10**8]*(N+1)
FROM = [0]*(N+1)
isUsed = defaultdict(lambda : defaultdict(bool))

def dijk(st):
    hq = []
    heapq.heappush(hq, [0, st])
    visited[st] = 0
    
    while hq:
        cost, now = heapq.heappop(hq)
        
        if visited[now] < cost: continue
        
        for next, c in route[now]:
            next_cost = cost + c
            if visited[next] > next_cost:
                visited[next] = next_cost
                FROM[next] = now
                heapq.heappush(hq, [next_cost, next])

dijk(1)

ans = 0
ans_list = []
for i in range(N, 0, -1):
    while FROM[i]:
        if not isUsed[i][FROM[i]]:
            isUsed[i][FROM[i]] = True
            ans += 1
            ans_list.append([i, FROM[i]])
        i = FROM[i]

print(ans)
for i in ans_list:
    print(*i)
