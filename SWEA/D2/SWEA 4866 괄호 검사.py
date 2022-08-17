TC = int(input())

for tc in range(1, TC+1):
    a = input()
    arr = []
    p = True
    for i in a:
        if i == '(' or i == '{':
            arr.append(i)
        elif i == ')':
            if not arr or arr[-1] != '(':
                p = False
                break
            else:
                arr.pop()
        elif i == '}':
            if not arr or arr[-1] != '{':
                p = False
                break
            else:
                arr.pop()
    if arr != []:
        p = False
        
    if p:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')