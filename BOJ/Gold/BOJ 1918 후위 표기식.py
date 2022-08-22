stk = []
n = input()
for i in n:
    if i.isalpha():
        print(i, end='')
    else:
        if stk == []:
            stk.append(i)
        elif i == '(':
            stk.append(i)
        elif i == '+' or i == '-':
            while True:
                if stk and stk[-1] != '(':
                    print(stk.pop(), end='')
                else:
                    stk.append(i)
                    break
        elif stk and (i == '*' or i == '/'):
            while True:
                if stk and (stk[-1] == '*' or stk[-1] == '/'):
                    print(stk.pop(), end='')
                else:
                    stk.append(i)
                    break
        elif i == ')':
            while True:
                if stk[-1] != '(':
                    print(stk.pop(), end='')
                else:
                    stk.pop()
                    break
while stk != []:
    print(stk.pop(), end='')