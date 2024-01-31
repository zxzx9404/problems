import sys, heapq

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()
hq = []
heapq.heappush(hq, arr[0][1])

for i in range(1, N):
    s, e = arr[i]
    if hq[0] <= s:
        heapq.heappop(hq)
    heapq.heappush(hq, e)

print(len(hq))
