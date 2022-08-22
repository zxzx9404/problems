for tc in range(1, 11): 
    n = int(input())
    s = input()
    stk = []
    huwi = []
    for i in s:
        if i.isdigit():                          # 숫자 형태면 후위에 추가
            huwi.append(i)
        else:
            if stk == []:                        # 숫자가 아니고 stk이 비었으면 추가
                stk.append(i)
            elif i == '+':                       # +보다 낮은 우선순위의 연산자는 없으므로 stk이 빌 때까지 pop
                while stk:
                    huwi.append(stk.pop())
                stk.append(i)
            elif i == '*':
                while True:
                    if stk and stk[-1] != '+':   # +가 나올때까지 pop
                        huwi.append(stk.pop())
                    else:
                        stk.append(i)
                        break
    while stk != []:                             # 남은것들 pop
        huwi.append(stk.pop())
        
    arr = []
    for j in huwi:
        if j.isdigit():                          # 숫자면 추가
            arr.append(j)
        else:
            if j == '+':                         # +면 뒤의 두 숫자를 꺼내서 더한 뒤 다시 집어넣음
                c = int(arr[-1]) + int(arr[-2])
                del arr[-1], arr[-1]
                arr.append(c)
            elif j == '*':
                c = int(arr[-1]) * int(arr[-2])  # *면 뒤의 두 숫자를 꺼내서 곱한 뒤 다시 집어넣음
                del arr[-1], arr[-1]
                arr.append(c)
    print(f'#{tc} {arr[0]}')                     # 정상적으로 종료되었다면, arr에는 1개의 원소(답)만이 남음