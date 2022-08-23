TC = int(input())
    
for tc in range(1, TC+1):    
    n = input().split()
    stk = []
    p = True
    print(f'#{tc}', end=' ')
    for char in n:
        if char not in '+-*/.':
            stk.append(char)
        else:
            if char == '.': # . 의 경우 아무 일도 일어나지 않음
                continue
            if len(stk) < 2: # 연산자가 들어왔는데 stk에 피연산자가 2개 미만이면 error
                print('error')
                p = False
                break
            else:
                x = int(stk.pop())
                y = int(stk.pop())

                if char == '+':
                    stk.append(y + x)
                elif char == '-':
                    stk.append(y - x)
                elif char == '*':
                    stk.append(y * x)
                elif char == '/':
                    stk.append(y // x)

    if p:
        if len(stk) == 1: 
            print(stk[0])
        else: # 모든 연산이 종료되었는데, stk에 피연산자가 2개 이상 남아있으면 error
            print('error')                                        