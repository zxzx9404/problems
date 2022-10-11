# 2차원과 개념적으로 동일한 3차원 델타 탐색
# Python3 : 4364ms / PyPy3 : 900ms
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 시작점들 찾기
q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                q.append((h, i, j))

# BFS 탐색
while q:
    h, i, j = q.popleft()
    
    for dh, di, dj in [[1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0]]:
        nh, ni, nj = h + dh, i + di, j + dj
        if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0:
            arr[nh][ni][nj] = arr[h][i][j] + 1
            q.append((nh, ni, nj))

ans = 0
for h in range(H):
    for i in range(N):
        # 0이 하나라도 남아있으면 -1 출력 후 break
        if 0 in arr[h][i]:
            print(-1)
            quit()
        ans = max(ans, max(arr[h][i]))
else:
    # 아니라면 제일 큰 값 -1 (시작점이 1이었으므로) 출력
    print(ans-1)