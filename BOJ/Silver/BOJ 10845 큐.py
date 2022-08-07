import sys
from collections import deque

dq=deque()

n=int(input())

for _ in range(n):
    h=sys.stdin.readline().strip().split()

    if h[0] == 'push':
        dq.append(int(h[1]))

    elif h[0] == 'pop':
        try:
            print(dq.popleft())
        except:
            print(-1)
 
    elif h[0] == 'size':
        print(len(dq))

    elif h[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)

    elif h[0] == 'front':
        try:
            print(dq[0])
        except:
            print(-1)

    elif h[0] == 'back':
        try:
            print(dq[-1])
        except:
            print(-1)

# queue에 관한 개념을 학습하라는 문제였는데 deque로 풀어도 될 것 같아서그냥 품
