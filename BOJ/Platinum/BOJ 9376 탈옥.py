# 첫 번째 죄수, 두 번째 죄수, 밖에서 구하러가는 사람
# 이 세명의 사람이 어느 한 점에서 만난다면 이들은 탈출이 가능하다 (밖에서 구하러 가는 사람이 접근한 장소 == 죄수 2명이 그 길을 그대로 따라가면 탈출 가능)
# 총 3번의 BFS를 돌려서 최소값을 구하면 되는 문제

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def bfs(si, sj):
    q = []
    q.append((0, si, sj))
    visited = [[10000]*(M+2) for _ in range(N+2)]
    visited[si][sj] = 0

    while q:
        cnt, i, j = heappop(q)
        
        if visited[i][j] > cnt:
            continue

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or ni == N+2 or nj < 0 or nj == M+2: continue
            if arr[ni][nj] == '*': continue
            if visited[ni][nj] <= visited[i][j]: continue
            if arr[ni][nj] == '#':
                if visited[ni][nj] > visited[i][j] + 1:
                    visited[ni][nj] = visited[i][j] + 1
                    heappush(q, (cnt+1, ni, nj))
            else:
                visited[ni][nj] = visited[i][j]
                heappush(q, (cnt, ni, nj))
    
    return visited

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    first = []
    second = []
    arr = []
    ans = 100000
    arr.append(['.']*(M+2))
    for _ in range(N):
        arr.append(['.']+list(input())+['.'])
    arr.append(['.']*(M+2))
    for i in range(N+2):
        for j in range(M+2):
            if arr[i][j] == '$':
                arr[i][j] = '.'
                if not first:
                    first = bfs(i, j)
                else:
                    second = bfs(i, j)
 
    outsider = bfs(0, 0)
    
    for i in range(N+2):
        for j in range(M+2):
            if first[i][j] != 10000 and second[i][j] != 10000 and outsider[i][j] != 10000:
                cnt = first[i][j] + second[i][j] + outsider[i][j]
                if arr[i][j] == '#':  # 문일 경우 3명이 전부 문을 통과했다고 카운트 되어있지만 실제로는 1번만 열면 되므로 -2 해줘야함
                    cnt -= 2
                if ans > cnt:
                    ans = cnt
                    # print(f'cnt : {cnt}, i : {i}, j : {j}, first : {first[i][j]}, second : {second[i][j]}, out: {outsider[i][j]}')
    
    print(ans)
