from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
visited = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    visited[a][b] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            if visited[i][k] and visited[k][j]:
                visited[i][j] = 1

for i in range(N):
    visited[i][i] = 1
    cnt = 0
    for j in range(N):
        if visited[i][j] or visited[j][i]:
            cnt += 1
    
    print(N - cnt)


