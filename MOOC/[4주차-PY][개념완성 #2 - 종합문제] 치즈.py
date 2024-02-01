def first_check(i, j):
    flag = False
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    
    temp = [(i, j)]
    q = [(i, j)]
    
    while q:
        i, j = q.pop()
        
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
        
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 0:
                q.append((ni, nj))
                temp.append((ni, nj))
                visited[ni][nj] = 1

                if ni == 0 or ni == N-1 or nj == 0 or nj == M-1:
                    flag = True
    
    if flag:
        out_sides.extend(temp)
    else:
        in_sides.append(temp)
    

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cheese = []
out_sides, in_sides = [], []
t = 0
ex_cheese = 0

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            cheese.append((i, j))
        else:
            if (i, j) not in out_sides:
                if in_sides:
                    for k in in_sides:
                        if (i, j) in k:
                            break
                    else:
                        first_check(i, j)
                else:
                    first_check(i, j)

while cheese:
    t += 1
    ex_cheese = len(cheese)
    temp = []
    idx = 0
    
    while idx < len(cheese):
        i, j = cheese[idx][0], cheese[idx][1]
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if (ni, nj) in out_sides:
                temp.append(cheese.pop(idx))
                break
        else:
            idx += 1
    
    if not cheese:
        break
    
    else:
        out_sides.extend(temp)
        
        if in_sides:
            idx = 0
            while idx < len(in_sides):
                p = False
                for i, j in in_sides[idx]:
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = i + di, j + dj
                        if (ni, nj) in out_sides:
                            out_sides.extend(in_sides.pop(idx))
                            p = True
                            break
                    if p:
                        break
                else:
                    idx += 1    

print(t)
print(ex_cheese)
