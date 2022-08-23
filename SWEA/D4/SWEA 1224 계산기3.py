def my_eval(word, stack):
    for char in word:
        # 피연산자를 stack에 담기
        if char not in '()+-*/':
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            if char == '-':
                stack.append(y - x)
            if char == '*':
                stack.append(y * x)
            if char == '/':
                stack.append(y / x)
    return stack[-1]


for tc in range(1, 11):
    n = int(input())
    wrd = input()
    stk = []
    
    result = ''

    for char in wrd:
        # 연산자
        if char in '*/+-()':
            if not stk:
                stk.append(char)
            elif char == '(':
                stk.append(char)
            elif char in '*/':
                while stk and stk[-1] in '*/':
                    result += stk.pop()
                stk.append(char)
            elif char in '+-':
                while stk and stk[-1] != '(':
                    result += stk.pop()
                stk.append(char)
            elif char == ')':
                while stk and stk[-1] != '(':
                    result += stk.pop()
                stk.pop()      

        # 피연산자
        else:
            result += char

    while stk:
        result += stk.pop()

    res = my_eval(result, [])

    print(f'#{tc} {res}')