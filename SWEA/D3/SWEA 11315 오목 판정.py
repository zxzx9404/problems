for TC in range(int(input())):
    N = int(input())
    box = [input() for _ in range(N)]
     
    p = False
    for i in range(N):
        for j in range(N):
            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [-1, 0, 1, -1, 1, -1, 0, 1]
            if box[i][j] == 'o':
                for c in range(8):
                    nx = i + dx[c]*4
                    ny = j + dy[c]*4
                    if 0 <= nx < N and 0 <= ny < N:
                        if box[nx][ny] =='o':
                            if box[i+dx[c]][j+dy[c]] == 'o' and box[i+dx[c]*2][j+dy[c]*2] == 'o' and box[i+dx[c]*3][j+dy[c]*3] == 'o':
                                p = True
                                break
            if p:
                break
        if p:
            break
                            
    if p:
        print(f'#{TC+1} YES')
    else:
        print(f'#{TC+1} NO')