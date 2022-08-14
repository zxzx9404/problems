TC = int(input())

for tc in range(TC):
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    while arr != []:
        if b == 0 and arr[b] == max(arr):
            count += 1
            break
        elif arr[0] == max(arr):
            arr.pop(0)
            count += 1
            b -= 1         
        else:
            arr.append(arr.pop(0))
            if b == 0:
                b = len(arr)-1
            else:
                b -= 1
    print(count)