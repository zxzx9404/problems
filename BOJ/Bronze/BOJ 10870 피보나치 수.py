def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n >= 3:
        return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))


#쉬운 문제는 따로 업로드하지 않으려고 했지만, 재귀의 기본 개념 학습용으로 업데이트