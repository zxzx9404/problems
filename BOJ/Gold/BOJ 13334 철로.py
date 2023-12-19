import heapq
import sys
input = sys.stdin.readline

N = int(input())
temp = [list(map(int, input().split())) for _ in range(N)]
D = int(input())
arr = []
for a, b in temp:
    if a > b:
        a, b = b, a
    if b - a <= D:
        arr.append([a, b])
arr.sort(key=lambda x : x[1])
ans = 0
hq = []
for road in arr:
    if not hq:
        heapq.heappush(hq, road)
    else:
        while hq and hq[0][0] < road[1] - D:
            heapq.heappop(hq)
        heapq.heappush(hq, road)
    ans = max(ans, len(hq))
print(ans)
