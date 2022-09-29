TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    hap = [[10000000000000]*N for _ in range(N)]

    q = [(0, 0)]
    hap[0][0] = 0

    while q:
        i, j = q.pop(0)

        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                cost = arr[ni][nj] - arr[i][j] + 1 if arr[ni][nj] - arr[i][j] > 0 else 1
                if hap[ni][nj] > hap[i][j] + cost:
                    hap[ni][nj] = hap[i][j] + cost
                    q.append((ni, nj))

    print(f'#{tc} {hap[N-1][N-1]}')
