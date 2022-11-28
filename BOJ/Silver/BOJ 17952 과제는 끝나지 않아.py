# PyPy3 : 556ms / Python3 : 1392ms

import sys
input = sys.stdin.readline

N = int(input())

stk = []
ans = 0

for i in range(N):
    task = list(map(int, input().split()))
    if task[0]:
        stk.append([task[1], task[2]])
    
    if stk:
        stk[-1][1] -= 1
    
        if not stk[-1][1]:
            ans += stk[-1][0]
            stk.pop()

print(ans)