from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
ST = int(input())

nodes = defaultdict(list)
visited = [6000000000]*(V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    nodes[u].append([v, w])

visited[ST] = 0
visited[0] = 0
hq = []
heapq.heapify(hq)
hq.append([0, ST])

while hq:
    sum_cost, now = heapq.heappop(hq)
    
    for next, cost in nodes[now]:
        if visited[next] > sum_cost + cost:
            visited[next] = sum_cost + cost
            heapq.heappush(hq, [sum_cost + cost, next])

for i in range(1, V+1):
    if i == ST:
        print(0)
    elif visited[i] == 6000000000:
        print("INF")
    else:
        print(visited[i])
