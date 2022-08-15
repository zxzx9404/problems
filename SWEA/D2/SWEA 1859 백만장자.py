TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    arr = list(map(int, input().split()))
    earn = 0
    maximum = 0
    for i in range(n-1, -1, -1):          # 뒤에서부터 최대값 탐색
        if maximum <= arr[i]:             # 클 경우 maximum에 저장
            maximum = arr[i]
        else:
            earn += maximum - arr[i]      # maximum보다 작을 경우 판매하여 이득 합산
    print(f'#{tc} {earn}')