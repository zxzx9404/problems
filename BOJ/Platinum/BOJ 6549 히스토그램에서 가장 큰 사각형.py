from collections import deque
import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    else:
        n = arr.pop(0)
        ans = deque()
        dap = 0
        for i in range(n):
            while ans and arr[ans[-1]] > arr[i]:
                imsi = ans.pop()
                if ans:
                    temp = arr[imsi] * (i - ans[-1] -1)
                else:
                    temp = arr[imsi] * i
                dap = max(dap, temp)
            ans.append(i)
        while ans:
            imsi = ans.pop()
            if ans:
                temp = arr[imsi] * (n - ans[-1] -1)
            else:
                temp = arr[imsi] * n
            dap = max(dap, temp)
        print(dap)