def len(n):
    cnt = 0
    for _ in n:
        cnt += 1
    return cnt

TC = int(input())

for tc in range(1, TC+1):
    s = input()
    arr = []
    for S in s:
        arr.append(S)
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            del arr[i], arr[i]
            if i == 0:
                continue
            else:
                i -= 1
        else:
            i += 1
    print(f'#{tc} {len(arr)}')