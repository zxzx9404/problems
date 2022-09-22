def perm(c, n, r):
    if c == r:
        print(*p)
    else:
        for i in range(n):
            if used[i] == 0:    # arr[i]가 사용되지 않았으면
                used[i] = 1     # 사용 처리
                p[c] = arr[i]   # p의 c번째 원소에 arr[i] 대입
                perm(c+1, n, r)    # 재귀 호출
                used[i] = 0     # 해제


N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * M

perm(0, N, M)