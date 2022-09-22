TC = int(input())

for tc in range(1, TC+1):
    n = float(input())
    ans = ''
    for i in range(1, 13):
        if n == 0:
            break
        if n >= 2**-i:
            ans += '1'
            n -= 2**-i
        else:
            ans += '0'
    print(f'#{tc}', end=' ')
    if n != 0:
        print('overflow')
    else:
        print(ans)