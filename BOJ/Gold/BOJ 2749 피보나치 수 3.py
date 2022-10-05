a = 0
b = 1


N = int(input())

if N == 1:
    print(a)
elif N == 2:
    print(b)
else:
    for _ in range(N):
        a, b = b%1000000, (a+b)%1000000
    print(a)