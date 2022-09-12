# 실행 시간 PyPy : 424ms / Python : 3732ms

TC = int(input())

for _ in range(TC):
    M, N, x, y = map(int, input().split())


    p = False
    j = x
    while j <= M*N:
        if (j-y) % N == 0:
            p = True
            break
        j += M
    if p:
        print(j)
    else:
        print(-1)