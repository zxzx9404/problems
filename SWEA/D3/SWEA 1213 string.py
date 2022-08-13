def Brute(T, P):
    i, j = 0, 0
    count = 0
    while i < len(T):
        if T[i] != P[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if len(P) == j:
            count += 1
            j = 0
    return count

for _ in range(10):
    n = int(input())
    P = input()
    T = input()
    num = Brute(T, P)
    print(f'#{n} {num}')
