import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [100000]*100001

visited[N] = 0
hq = []
heapq.heapify(hq)
hq.append([0, N])

while hq:
    sum_cost, now = heapq.heappop(hq)
    
    for next, cost in [[now - 1, 1], [now + 1, 1], [now * 2, 0]]:
        if next > 100000: continue
        if next < 0: continue
        if visited[next] > sum_cost + cost:
            visited[next] = sum_cost + cost
            heapq.heappush(hq, [sum_cost + cost, next])

print(visited[K])
