di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def flood_fill(n):
    visited = [[0]*N for _ in range(N)]
    num_of_group = 0
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] > n and not visited[i][j]:
                num_of_group += 1
                
                q = []
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    y, x = q.pop()
                    
                    for k in range(4):
                        ni, nj = y + di[k], x + dj[k]
                        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] > n:
                            visited[ni][nj] = 1
                            q.append((ni, nj))

    return num_of_group

N = int(input())
arr = []
max_height = 1
ans = 1
for i in range(N):
    t = list(map(int, input().split()))
    max_height = max(max_height, max(t))
    arr.append(t)


for i in range(1, max_height):
    ans = max(ans, flood_fill(i))

print(ans)
