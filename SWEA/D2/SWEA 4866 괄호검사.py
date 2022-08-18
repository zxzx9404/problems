TC = int(input())

for tc in range(1, TC+1):
    a = input()
    arr = []
    p = True   # 반복문 탈출용 변수
    for i in a:
        if i == '(' or i == '{':  # 여는 괄호일 경우 집어넣기
            arr.append(i)
        elif i == ')':
            if not arr or arr[-1] != '(':  # 닫는 괄호가 나온 경우, 스택이 비어있어도 안되고, 앞이 '('이 아니어도 안됨
                p = False
                break
            else:
                arr.pop() # 조건에 맞을 경우 한 쌍이 된 '('와 ')'를 제거 // '{' '}' 도 똑같은 매커니즘
        elif i == '}':
            if not arr or arr[-1] != '{':
                p = False
                break
            else:
                arr.pop()
    if arr != []:   # 리스트를 순회한 뒤에 남아있는 괄호가 있으면 안 됨
        p = False
        
    if p:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')