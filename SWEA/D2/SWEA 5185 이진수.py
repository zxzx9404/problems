TC = int(input())

for tc in range(1, TC+1):
    n, m = input().split()
    n = int(n)
    print(f'#{tc}', end=' ')
    for i in m:
        if i.isdigit():
            ans = str(bin(int(i)))[2:]
        else:
            ans = str(bin(ord(i)-55))[2:]
        if len(ans) != 4:
            ans = '0'*(4-len(ans)) + ans
        print(ans, end='')
    print()