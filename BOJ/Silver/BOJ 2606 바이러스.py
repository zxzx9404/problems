N = int(input())
w = int(input())
arr, arr2 = [], []
p = False
for _ in range(w):
    arr.append(list(map(int, input().split())))
i = 0
while i < len(arr):
    if arr[i][0] == 1:
        arr2.extend(arr.pop(i))
        i = 0
    elif arr[i][1] == 1:
        arr2.extend(arr.pop(i))
        i = 0
    else:
        i += 1

if arr2 == []:
    p = True

i = 0
while i < len(arr):
    if arr[i][0] in arr2:
        arr2.extend(arr.pop(i))
        i = 0
    elif arr[i][1] in arr2:
        arr2.extend(arr.pop(i))
        i = 0
    else:
        i += 1

ans = len(set(arr2))
if p:
    print(0)
else:
    print(ans-1)