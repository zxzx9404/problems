import sys
sys.setrecursionlimit(10000000)


def bug(i, j):
    temp_i = i
    while 0 <= temp_i+1 < N and arr[temp_i+1][j] != 0 :
        temp_i += 1
        arr[temp_i][j] = 0
        bug(temp_i, j)
    temp_i = i
    while 0 <= temp_i-1 < N and arr[temp_i-1][j] != 0:
        temp_i -= 1
        arr[temp_i][j] = 0
        bug(temp_i, j)
    temp_j = j
    while 0 <= temp_j+1 < M and arr[i][temp_j+1] != 0:
        temp_j += 1
        arr[i][temp_j] = 0
        bug(i, temp_j)
    temp_j = j
    while 0 <= temp_j-1 < M and arr[i][temp_j-1] != 0:
        temp_j -= 1
        arr[i][temp_j] = 0
        bug(i, temp_j)



TC = int(input())

for tc in range(TC):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    baechu = []
    for _ in range(K):
        baechu.append(list(map(int, input().split())))
    for x, y in baechu:
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                bug(i, j)

    print(cnt)