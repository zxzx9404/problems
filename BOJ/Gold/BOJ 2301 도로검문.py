import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N)]
roads = [[0]*N for _ in range(N)]
FROM = [i for i in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    adj[a].append(b)
    adj[b].append(a)
    roads[a][b] = t
    roads[b][a] = t


hq = []
heappush(hq, [0, 0])
vst = [sys.maxsize]*N
vst[0] = 0
while hq:
    cost, now = heappop(hq)
    
    if vst[now] < cost: continue
    
    for next in adj[now]:
        nc = cost + roads[now][next]
        if vst[next] > nc:
            vst[next] = nc
            FROM[next] = now
            heappush(hq, [nc, next])


if vst[N-1] == sys.maxsize:
    print(0)
    quit()

original_time = vst[N-1]
new_time = 0
a = N-1
b = FROM[N-1]

while True:
    saved_c = roads[a][b]
    roads[a][b] = sys.maxsize
    roads[b][a] = sys.maxsize
    
    hq = []
    heappush(hq, [0, 0])
    vst = [sys.maxsize]*N
    vst[0] = 0
    while hq:
        cost, now = heappop(hq)

        if vst[now] < cost: continue

        for next in adj[now]:
            nc = cost + roads[now][next]
            if vst[next] > nc:
                vst[next] = nc
                FROM[next] = now
                heappush(hq, [nc, next])
    
    if vst[N-1] == sys.maxsize:
        print(-1)
        quit()
    
    new_time = max(new_time, vst[N-1]-original_time)
    
    
    roads[a][b] = saved_c
    roads[b][a] = saved_c
    
    a, b = b, FROM[b]
    
    if not a:
        break


print(new_time)
