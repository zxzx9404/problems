TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    i = 1
    p = True
    while True:
        # 세제곱근이니?
        if i**3 == n:
            # 맞으면 나가
            break
        # 다음손님 오실게요~
        i += 1
        # 엥 찾을 값보다 커졌어?
        if i**3 > n:
            p = False
            # 나가임마
            break
    if p:
        print(f'#{tc} {i}')
    else:
        print(f'#{tc} -1')