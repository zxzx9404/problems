# 여러개의 시작점을 가진 BFS
# 실행시간 Python3 : 2640ms / PyPy3 : 472ms
from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 시작점들 찾기
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))
            
# BFS 탐색
while q:
    i, j = q.popleft()
    
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            arr[ni][nj] = arr[i][j] + 1
            q.append((ni, nj))

ans = 0
for i in range(N):
    # 0이 하나라도 남아있으면 -1 출력 후 break
    if 0 in arr[i]:
        print(-1)
        quit()
    ans = max(ans, max(arr[i]))
else:
    # 아니라면 제일 큰 값 -1 (시작점이 1이었으므로) 출력
    print(ans-1)