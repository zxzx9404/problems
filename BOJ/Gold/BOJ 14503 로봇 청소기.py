N, M = map(int, input().split())
i, j, dir = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

next = (i, j, dir)

cnt = 1
arr[i][j] = 2

while next:
    i, j, dir = next

    for _ in range(4):
        dir = (dir + 3) % 4
        ni = i + delta[dir][0]
        nj = j + delta[dir][1]

        if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
            arr[ni][nj] = 2
            cnt += 1
            next = (ni, nj, dir)
            break
    else:
        b_i = i + delta[(dir+2)%4][0]
        b_j = j + delta[(dir+2)%4][1]

        if 0 <= b_i < N and 0 <= b_j < M and arr[b_i][b_j] != 1:
            next = (b_i, b_j, dir)
        else:
            next = 0

print(cnt)