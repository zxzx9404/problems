def power_check(i, j, team):
    stk = [(i, j)]
    field[i][j] = False
    how_many = 1
    
    while stk:
        i, j = stk.pop()
        
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == team:
                field[ni][nj] = False
                how_many += 1
                stk.append((ni, nj))
    
    powers[team] += how_many ** 2 
                                    

M, N = map(int, input().split())

powers = {'W' : 0, 'B' : 0}

field = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if field[i][j]:
            power_check(i, j, field[i][j])

print(powers['W'], powers['B'])