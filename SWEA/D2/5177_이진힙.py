# 최소힙을 유지하며 삽입을 하기 위한 함수
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    heap = [0]*(n+1)
    last = 0
    arr = list(map(int, input().split()))
    for i in arr:
        enq(i)
    p = n
    ans = 0
    # 조상 노드 찾아서 합 구하기
    while p > 0:
        c = p // 2
        ans += heap[c]
        p = c
    print(f'#{tc} {ans}')