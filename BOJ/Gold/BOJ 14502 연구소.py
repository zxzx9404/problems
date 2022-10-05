## pypy로만 통과

def bfs(cnt):
    if cnt == 3:
        global ans
        
        qq = q[:]
        temp = 0
        back = []
        while qq:
            y, x = qq.pop(0)
            
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = y + di, x + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                    temp += 1
                    arr[ni][nj] = 2
                    qq.append((ni, nj))
                    back.append((ni, nj))
                    
                    if count-temp < ans:
                        break
                    
        ans = max(ans, count-temp)
        while back:
            y, x = back.pop()
            arr[y][x] = 0
        return
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                bfs(cnt + 1)
                arr[i][j] = 0

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


ans = 0
q = []

count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            q.append((i, j))
        elif arr[i][j] == 0:
            count += 1

count -= 3

bfs(0)

print(ans)