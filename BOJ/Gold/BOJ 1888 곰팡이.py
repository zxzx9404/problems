from collections import defaultdict

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
ans = 0

def how_many_union():
    visited = [[0]*M for _ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j]:
                temp += 1
                visited[i][j] = 1
                q = [(i, j)]
                while q:
                    y, x = q.pop()
                    for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                        ni, nj = y + di, x + dj
                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj]:
                            visited[ni][nj] = 1
                            q.append((ni, nj))
    
    return temp



while True:
    visited = [[0]*M for _ in range(N)]
    gompang = defaultdict(list)
    
    # 0일차
    if how_many_union() == 1:
        print(ans)
        break
    
    # 곰팡이 무리 찾기
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j]:
                visited[i][j] = 1
                q = [(i, j)]
                gompang[arr[i][j]].append((i, j))
                while q:
                    y, x = q.pop()
                    for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                        ni, nj = y + di, x + dj
                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == arr[i][j]:
                            visited[ni][nj] = 1
                            q.append((ni, nj))
                            gompang[arr[i][j]].append((ni, nj))
    

    # 곰팡이 순회하면서 값 바꿔주기
    for a in gompang.items():
        key, value = a[0], a[1]
        while value:
            y, x = value.pop()
            for n in range(y-key, y+key+1):
                for m in range(x-key, x+key+1):
                    if 0 <= n < N and 0 <= m < M and key > arr[n][m]:
                        arr[n][m] = key

    
    # # 무리가 몇개인지 다시 찾기
    # visited = [[0]*M for _ in range(N)]
    # temp = 0
    # for i in range(N):
    #     for j in range(M):
    #         if not visited[i][j] and arr[i][j]:
    #             temp += 1
    #             visited[i][j] = 1
    #             q = [(i, j)]
    #             while q:
    #                 y, x = q.pop()
    #                 for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
    #                     ni, nj = y + di, x + dj
    #                     if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj]:
    #                         visited[ni][nj] = 1
    #                         q.append((ni, nj))
    ans += 1
    
    # if temp == 1:
    #     print(ans)
    #     break