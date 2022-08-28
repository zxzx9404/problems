TC = int(input())

for tc in range(1, TC+1):
    N, P = map(int, input().split())
    if N % P == 0:
        print(f'#{tc} {(N//P)**P}')
    else:
        gop = 1
        for i in range(N % P):
            gop *= ((N // P) + 1)
        for j in range(P - (N % P)):
            gop *= (N//P)
        print(f'#{tc} {gop}')