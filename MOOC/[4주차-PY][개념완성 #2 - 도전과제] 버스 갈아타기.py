from sys import stdin
from collections import deque


def solution():
    # input
    input = stdin.readline
    m, n = map(int, input().split())
    k = int(input())
    BUS = [0] * (k+1)
    for _ in range(k):
        b, x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        BUS[b] = (x1, y1, x2, y2)
    sx, sy, dx, dy = map(int, input().split())

    # bfs
    visited = [0] * (k+1)
    queue = deque()
    for i in range(1, k+1):
        if BUS[i][0] <= sx <= BUS[i][2] and BUS[i][1] <= sy <= BUS[i][3]:
            queue.append(i)
            visited[i] = 1
    answer = 0
    while queue:
        bnum = queue.popleft()
        if BUS[bnum][0] <= dx <= BUS[bnum][2] and BUS[bnum][1] <= dy <= BUS[bnum][3]:
            answer = visited[bnum]
            break
        for nbnum in range(1, k+1):
            if not visited[nbnum]:
                if BUS[bnum][0] <= BUS[nbnum][2] and BUS[bnum][2] >= BUS[nbnum][0] and BUS[bnum][1] <= BUS[nbnum][3] and BUS[bnum][3] >= BUS[nbnum][1]:
                    visited[nbnum] = visited[bnum] + 1
                    queue.append(nbnum)
    print(answer)


solution()
