# 플로이드 워셜
# PyPy3로만 통과

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
visited = [[1e12]*N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    visited[a][b] = c


for k in range(N):
    for i in range(N):
        for j in range(N):
            visited[i][j] = min(visited[i][j], visited[i][k] + visited[k][j])

ans = 1e12
for i in range(N):
    for j in range(N):
        if visited[i][j] and visited[j][i]:
            ans = min(ans, visited[i][j] + visited[j][i])

if ans == 1e12:
    ans = -1

print(ans)
