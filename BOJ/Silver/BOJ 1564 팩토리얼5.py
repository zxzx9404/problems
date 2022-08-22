n = int(input())

fac = 1

for i in range(2, n+1):
    fac *= i
    while str(fac)[-1] == '0':
        fac //= 10  
    fac %= 10000000000000
print(str(fac)[-5:])


'''
해결하지 못한 의문

fac %= 10000000000000 (10조)를 하니 정답인데,
fac %= 100000000000 (1천억)은 오답이다.

왜그럴까..?
'''
