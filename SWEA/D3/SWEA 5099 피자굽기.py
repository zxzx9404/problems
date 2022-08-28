TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # 화덕 안의 피자들의 번호를 기억할 리스트
    lst = []
    # 화덕 내부 리스트
    oven = []

    for t in range(n):
        # 화덕에 피자를 넣음 (화덕의 크기만큼)
        oven.append(arr.pop(0))
        # lst에 번호를 저장 : 초기값 [1, 2, 3, ..., n]
        lst.append(t+1)
    idx = 1 # 번호 계산용 index
    p = True # 반복문 탈출용 bool
    while p:
        for i in range(n):
            # 본인이 마지막 피자라면, 화덕 내부 치즈 값 == 본인의 치즈 값
            if sum(oven) == oven[i]:
                p = False
                break
            # 아닐 경우 치즈의 양을 2로 나눔
            oven[i] = oven[i] // 2
            # 피자가 다 익었고, 아직 투입하지 않은 피자가 있다면 넣어줌
            if oven[i] == 0 and arr:
                oven[i] = arr.pop(0)
                lst[i] = n+idx
                idx += 1
    print(f'#{tc} {lst[i]}')
