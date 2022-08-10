from collections import deque
import sys

deque1 = deque()

n = int(input())

for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push_front':
        deque1.appendleft(a[1])
    if a[0] == 'push_back':
        deque1.append(a[1])
    if a[0] == 'pop_front':
        if deque1:
            print(deque1.popleft())
        else:
            print(-1)
    if a[0] == 'pop_back':
        if deque1:
            print(deque1.pop())
        else:
            print(-1)
    if a[0] =='size':
        print(len(deque1))
    if a[0] == 'empty':
        if deque1:
            print(0)
        else:
            print(1)
    if a[0] == 'front':
        if deque1:
            print(deque1[0])
        else:
            print(-1)
    if a[0] == 'back':
        if deque1:
            print(deque1[-1])
        else:
            print(-1)