TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_danzo = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                danzo = arr[i]*arr[j]
                for k in range(len(str(danzo))-1):
                        if int(str(danzo)[k]) > int(str(danzo)[k+1]):
                            break
                else:
                    if max_danzo <= danzo:
                        max_danzo = danzo
    if max_danzo == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_danzo}')