TC = int(input())

for tc in range(1, TC+1):
    bong = input()
    count = 0
    temp = 0
    for i in range(len(bong)):
        if bong[i] == '(' and bong[i+1] != ')':
            temp += 1
        elif bong[i] == '(' and bong[i+1] == ')':
            count += temp
        elif bong[i] == ')' and bong[i-1] != '(':
            temp -= 1
            count += 1
    print(f'#{tc} {count}')