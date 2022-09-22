TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().split())
    cargo = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    ans = 0
    # 화물, 트럭을 내림차순 정렬
    cargo.sort(reverse=True)
    truck.sort(reverse=True)
    # 트럭, 화물 인덱스
    i, j = 0, 0
    while True:
        # 내림차순 정렬이므로, 실을 수 있으면 무조건 싣기
        if truck[i] >= cargo[j]:
            ans += cargo[j]
            i += 1
        j += 1
        
        if m == i or n == j:
            break
    
    print(f'#{tc} {ans}')