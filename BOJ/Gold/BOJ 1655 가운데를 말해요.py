import sys
import heapq
input = sys.stdin.readline

q1 = []
q2 = []

N = int(input())

for i in range(N):
    n = int(input())
    
    if len(q1) == len(q2):
        heapq.heappush(q1, (-n, n))
    else:
        heapq.heappush(q2, (n, n))

    if q2 and q1[0][1] > q2[0][0]:
        a = heapq.heappop(q2)[1]
        b = heapq.heappop(q1)[1]
        
        heapq.heappush(q1, (-a, a))
        heapq.heappush(q2, (b, b))

    print(q1[0][1])
