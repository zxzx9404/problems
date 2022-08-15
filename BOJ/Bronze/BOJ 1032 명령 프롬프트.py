N = int(input())

arr = []
ans = ''
for _ in range(N):
    arr.append(input())


for i in range(len(arr[0])):
    p = True
    for j in range(N-1):
        if arr[j][i] != arr[j+1][i]:
            p = False
    if p:
        ans += arr[0][i]
    else:
        ans += '?'
print(ans)