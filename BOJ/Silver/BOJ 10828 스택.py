import sys

N = int(input())
stack = []

for i in range(N):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        stack.append(a[1])
    if a[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if a[0] == 'size':
        print(len(stack))
    if a[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    if a[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)