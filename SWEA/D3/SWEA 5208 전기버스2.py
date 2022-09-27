TC = int(input())

for tc in range(1, TC+1):
    arr = list(map(int, input().split()))
    n = arr[0]
    cnt = 0

    i = 1
    while True:
        if arr[i] + i >= n:
            cnt += 1
            n, i = i, 0
            if arr[1] + 1 >= n:
                break
        i += 1

    print(f'#{tc} {cnt}')