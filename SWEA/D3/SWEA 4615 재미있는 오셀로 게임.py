def dol1(i, j, k):
    global p
    # 아래쪽 방향 재귀식
    if 0 <= i+1 < N and pan[i+1][j] != 0 and pan[i+1][j] != k:
        dol1(i+1, j, k)
        if p:
            pan[i][j] = k
    else:
        if i+1 >= N or i+1 < 0 or pan[i+1][j] == 0:
            if pan[i][j] == k:
                p = True
        else:
            if pan[i+1][j] == k:
                pan[i][j] = k
                p = True

def dol2(i, j, k):
    global p
    # 위쪽 방향 재귀식
    if 0 <= i-1 < N and pan[i-1][j] != 0 and pan[i-1][j] != k:
        dol2(i-1, j, k)
        if p:
            pan[i][j] = k
    else:
        if i-1 >= N or i-1 < 0 or pan[i-1][j] == 0:
            if pan[i][j] == k:
                p = True
        else:
            if pan[i-1][j] == k:
                pan[i][j] = k
                p = True

def dol3(i, j, k):
    global p
    # 우측 방향 재귀식
    if 0 <= j+1 < N and pan[i][j+1] != 0 and pan[i][j+1] != k:
        dol3(i, j+1, k)
        if p:
            pan[i][j] = k
    else:
        if j+1 >= N or j+1 < 0 or pan[i][j+1] == 0:
            if pan[i][j] == k:
                p = True
        else:
            if pan[i][j+1] == k:
                pan[i][j] = k
                p = True

def dol4(i, j, k):
    global p
    # 좌측 방향 재귀식
    if 0 <= j-1 < N and pan[i][j-1] != 0 and pan[i][j-1] != k:
        dol4(i, j-1, k)
        if p:
            pan[i][j] = k
    else:
        if j-1 >= N or j-1 < 0 or pan[i][j-1] == 0:
            if pan[i][j] == k:
                p = True
        else:
            if pan[i][j-1] == k:
                pan[i][j] = k
                p = True

def dol5(i, j, k):
    global p
    #  우하방향 대각선 재귀식
    if 0 <= i+1 < N and 0 <= j+1 < N and pan[i+1][j+1] != 0 and pan[i+1][j+1] != k:
        dol5(i+1, j+1, k)
        if p:
            pan[i][j] = k
    else:
        if i+1 >= N or i+1 < 0 or j+1 >= N or j+1 < 0 or pan[i+1][j+1] == 0:
            if pan[i][j] == k:
                p = True
        else:
            if pan[i+1][j+1] == k:
                pan[i][j] = k
                p = True

def dol6(i, j, k):
    global p
    #  우상방향 대각선 재귀식
    if 0 <= i-1 < N and 0 <= j+1 < N and pan[i-1][j+1] != 0 and pan[i-1][j+1] != k:
        dol6(i-1, j+1, k)
        if p:
            pan[i][j] = k
    else:
        if i-1 >= N or i-1 < 0 or j+1 >= N or j+1 < 0 or pan[i-1][j+1] == 0:
            if pan[i][j] == k:
                p = True
        else:
            if pan[i-1][j+1] == k:
                pan[i][j] = k
                p = True

def dol7(i, j, k):
    global p
    #  좌상방향 대각선 재귀식
    if 0 <= i-1 < N and 0 <= j-1 < N and pan[i-1][j-1] != 0 and pan[i-1][j-1] != k:
        dol7(i-1, j-1, k)
        if p:
            pan[i][j] = k
    else:
        if i-1 >= N or i-1 < 0 or j-1 >= N or j-1 < 0 or pan[i-1][j-1] == 0:
            if pan[i][j] == k:
                p = True
        else:
            if pan[i-1][j-1] == k:
                pan[i][j] = k
                p = True

def dol8(i, j, k):
    global p
    #  좌하방향 대각선 재귀식
    if 0 <= i+1 < N and 0 <= j-1 < N and pan[i+1][j-1] != 0 and pan[i+1][j-1] != k:
        dol8(i+1, j-1, k)
        if p:
            pan[i][j] = k
    else:
        if i+1 >= N or i+1 < 0 or j-1 >= N or j-1 < 0 or pan[i+1][j-1] == 0:
            if pan[i][j] == k:
                p = True
        else:
            if pan[i+1][j-1] == k:
                pan[i][j] = k
                p = True

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = []
    # 좌표값 추가
    for _ in range(M):
        arr.append(list(map(int, input().split())))
    # 기본 배치 추가
    pan = [[0] * N for _ in range(N)]
    pan[(N//2)-1][(N//2)-1] = 2
    pan[N//2][N//2] = 2 
    pan[(N//2)-1][N//2] = 1
    pan[(N//2)][(N//2)-1] = 1

    # 8 방위 탐색
    for j, i, k in arr:
        pan[i-1][j-1] = k
        p = False
        dol1(i-1, j-1, k)
        p = False
        dol2(i-1, j-1, k)
        p = False
        dol3(i-1, j-1, k)
        p = False
        dol4(i-1, j-1, k)
        p = False
        dol5(i-1, j-1, k)
        p = False
        dol6(i-1, j-1, k)
        p = False
        dol7(i-1, j-1, k)
        p = False
        dol8(i-1, j-1, k)

    # 수 세기
    b = 0
    w = 0
    for i in pan:
        b += i.count(1)
        w += i.count(2)

    print(f'#{tc} {b} {w}')
