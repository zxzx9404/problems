def fibo(n):
    a, b = 1, 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        for i in range(1, n):
            a, b = b, a+b
        return b


n = int(input())

ans = fibo(n)%10007

print(ans)

# 저기서 return a 로 바꾸면 재귀 없이 피보나치 구현하는 법임