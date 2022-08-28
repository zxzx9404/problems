TC = int(input())

for tc in range(1, TC+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    # 첫 붕어빵이 만들어지는 시간보다 첫 손님의 방문이 빠를 경우 불가능
    if M > arr[0]:
        print(f'#{tc} Impossible')
    else:
        jaego, t = K, M
        # 가능여부 판단용 변수
        p = True
        # 아직 안온 손님이 있을 경우
        while arr:
            # 손님이 있고, 손님의 도착시간이 된 경우
            while arr and arr[0] == t:
                # 재고가 있다면 서빙 후 손님 삭제
                if jaego:
                    jaego -= 1
                    del arr[0]
                # 서빙할 수 없다면 p = False 후 break
                else:
                    p = False
                    break
            # 시간 1 증가
            t += 1
            # 붕어빵이 만들어질 시간이 되었다면 재고 추가
            if t % M == 0:
                jaego += K

            # 안쪽 while문에서 서빙 불가 판정을 받은 경우 break
            if not p:
                break
        if p:
            print(f'#{tc} Possible')
        else:
            print(f'#{tc} Impossible')