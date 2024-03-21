from collections import defaultdict

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def solution(land):

    N, M = len(land), len(land[0])
    group_have = dict()
    group_in_col = defaultdict(set)
    group_cnt = 0
    for i in range(N):
        for j in range(M):
            if land[i][j]:
                q = []
                q.append((i, j))
                cnt = 1
                land[i][j] = 0
                group_cnt += 1
                while q:
                    y, x = q.pop()
                    group_in_col[x].add(group_cnt)
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < N and 0 <= nx < M and land[ny][nx]:
                            land[ny][nx] = 0
                            cnt += 1
                            q.append((ny, nx))

                group_have[group_cnt] = cnt
    
    ans = 0
    
    for k, v in group_in_col.items():
        t = 0
        for g in v:
            t += group_have[g]
        ans = max(ans, t)
    
    return ans
