# python3 : 864ms

def dfs(q):
    global ans
    p = False
    back = []
    qq = q[:]
    for i, j in can_virus:
        if (i, j) not in qq:
            arr[i][j] = 0
    while qq:
        i, j = qq.pop(0)
        
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
                arr[ni][nj] = arr[i][j] + 1
                qq.append((ni, nj))
                back.append((ni, nj))
                if arr[ni][nj] > ans:
                    p = True
                    break
        if p:
            break
    if not p:
        temp = max(sum(arr, []))
        if ans > temp and not sum(arr, []).count(0):
            ans = temp

    while back:
        i, j = back.pop()
        arr[i][j] = 0
    
    for i, j in can_virus:
        arr[i][j] = 2

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

ans = N*N
can_virus = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            can_virus.append((i, j)) 

n = len(can_virus)

for i in range(1<<n):
    temp = []
    for j in range(n):
        if i & (1<<j):
            temp.append(can_virus[j])
        if len(temp) > M:
            break
    if len(temp) == M:
        dfs(temp)

if ans == N*N:
    print(-1)
else:
    print(ans-2)