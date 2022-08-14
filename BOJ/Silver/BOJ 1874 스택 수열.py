n = int(input())

arr = []
temp = []
arr2 = []
for i in range(n, 0, -1):
    arr.append(i)

ans = []
for i in range(n):
    ans.append(int(input()))

i = 0
dap = []
p = True
while arr2 != ans:
    if temp == []:
        temp.append(arr.pop())
        dap.append('+')
    elif ans[i] == temp[-1]:
        arr2.append(temp.pop())
        dap.append('-')
        i += 1
    elif arr == []:
        print('NO')
        p = False
        break
    elif ans[i] != temp[-1]:
        temp.append(arr.pop())
        dap.append('+')


if p:
    for i in dap:
        print(i)
