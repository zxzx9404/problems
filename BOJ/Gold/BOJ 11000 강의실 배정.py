import heapq

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x : (x[0], x[1]))
hq = []
ans = 1
heapq.heappush(hq, arr[0][1])
if len(arr) == 1:
    print(1)
else:
    for s, e in arr[1:]:
        while hq:
            t = heapq.heappop(hq)
            if t > s:
                heapq.heappush(hq, t)
                break
        
        heapq.heappush(hq, e)
        ans = max(ans, len(hq))
    
    print(ans)
