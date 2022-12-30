M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
ans = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        arr[i][x1:x2] = [1]*(x2-x1)

for _i in range(M):
    for _j in range(N):
        if not arr[_i][_j]:
            arr[_i][_j] = 2
            stk = [(_i, _j)]
            temp = 1
            while stk:
                i, j = stk.pop()
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < M and 0 <= nj < N and not arr[ni][nj]:
                        arr[ni][nj] = 2
                        temp += 1
                        stk.append((ni, nj))
            ans.append(temp)

print(*sorted(ans))