from collections import deque

def maximum_length(st_i, st_j):
    visited = [[0]*(M+2) for _ in range(N+2)]
    visited[st_i][st_j] = 1
    
    deq = deque([[st_i, st_j, 0]])
    
    while deq:
        i, j, cnt = deq.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if arr[ni][nj] == 'L' and not visited[ni][nj]:
                visited[ni][nj] = 1
                deq.append((ni, nj, cnt + 1))
    
    return cnt

N, M = map(int, input().split())
arr = [[0] + list(input()) + [0] if 1<=r<=N else [0]*(M+2) for r in range(N+2)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


q_start = deque()
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == 'L':
            q_start.append((i, j))

ans = list()
for i, j in q_start:
    ans.append(maximum_length(i, j))

print(max(ans))
