# DFS
N, M = map(int, input().split())
M -= 1
metro = [list(map(int, input().split())) for _ in range(N)]

ans = 10000
visited = [10000]*N
route = []

def dfs(now, mins, way):
    global ans, route
    
    if mins > visited[now]:
        return
    
    for i in range(N):
        if i != now and visited[i] > mins + metro[now][i] and ans > mins + metro[now][i]:
            visited[i] = mins + metro[now][i]
            
            if i == M and ans > mins + metro[now][i]: 
              ans = mins + metro[now][i]
              route = way + [M]
            else:
                dfs(i, mins + metro[now][i], way + [i])


dfs(0, 0, [0])
print(ans)
for i in route:
    print(i+1, end=" ")
