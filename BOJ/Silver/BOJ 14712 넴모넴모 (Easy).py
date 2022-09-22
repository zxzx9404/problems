def dfs(cnt):
    global ans
    if cnt == N * M:
        ans += 1
        return
    
    i = cnt // M
    j = cnt % M
    
    dfs(cnt + 1)
    if (0 > i-1 or arr[i-1][j] == 0) or (0 > j-1 or arr[i][j-1] == 0) or ((0 > i-1 and 0 > j-1) or arr[i-1][j-1] == 0): 
        arr[i][j] = 1
        dfs(cnt + 1)
        arr[i][j] = 0
        
        
N, M = map(int, input().split())
arr = [[0]*(M) for _ in range(N)]

ans = 0

dfs(0)
print(ans)