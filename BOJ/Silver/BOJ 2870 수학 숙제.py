import heapq

N = int(input())
heap = []

for _ in range(N):
    word = input()
    num = ''
    for i in word:
        if i.isdigit():
            num += i
        elif num:
            heapq.heappush(heap, int(num))
            num = ''
    if num:
        heapq.heappush(heap, int(num))

while heap:
    print(heapq.heappop(heap))