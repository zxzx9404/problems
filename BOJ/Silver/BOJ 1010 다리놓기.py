t = int(input())

for _ in range(t):
    a = 1
    n, m = map(int, input().split())
    if n == m:
        print(1)
        continue
    elif n == 0:
        print(0)
        continue
    for j in range(1, m+1):
        a *= j
        if j == n:
            b = a
        if j == m-n:
            c = a
    print(int(a/(b*c)))
    
#팩토리얼 함수를 선언하여 해결할 수도 있지만, 처음 머릿속에 떠오른 방법대로 풀어봄