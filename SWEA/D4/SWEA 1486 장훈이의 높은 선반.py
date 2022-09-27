TC = int(input())

for tc in range(1, TC+1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    # 일단 차이를 목표값으로 설정
    ans = b
    # 비트 연산자를 활용하여 부분집합 만들기
    for i in range(1<<n):
        temp = 0
        for j in range(n):
            if i & (1<<j):
                temp += arr[j]
                # 현재 최소값보다 크다면 break
                if temp > b + ans:
                    break
        # 목표값 == 최소값인 점을 찾았다면 바로 탐색 종료
        if temp == b:
            ans = 0
            break
        # 목표값보다 큰 값을 찾았다면 현재 최소값과 비교하여 저장
        elif temp > b:
            ans = min(temp - b, ans)
            
    print(f'#{tc} {ans}')