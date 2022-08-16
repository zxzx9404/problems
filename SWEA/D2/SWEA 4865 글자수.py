TC = int(input())

for tc in range(1, TC+1):
    A = input()
    B = input()
    max = 0
    for i in A:           # 패턴 문자열을 순회
        temp = 0
        for j in B:       # 타겟 문자열을 순회하며 패턴 문자를 하나씩 검색
            if i == j:
                temp += 1
        if max <= temp:   # max보다 클경우 max에 저장
            max = temp
    print(f'#{tc} {max}')