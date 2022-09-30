# 실행 시간 : 904ms

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
ans = 10**12

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))

for i in range(1<<len(chicken)):
    visited = [0] * len(chicken)
    for j in range(len(chicken)):
        if i & (1<<j):
            visited[j] = 1
    if sum(visited) == M:
        temp = 0
        for ii, jj in house:
            temp2 = 10**10
            for k in range(len(chicken)):
                if visited[k]:
                    temp2 = min(temp2, abs(chicken[k][0]-ii) + abs(chicken[k][1]-jj))
            temp += temp2
        ans = min(temp, ans)     

print(ans)