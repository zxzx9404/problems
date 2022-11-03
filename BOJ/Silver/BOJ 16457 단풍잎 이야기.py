# Python3 : 976ms, PyPy3 : 380ms

def dfs(cnt, next):
    if cnt == N:
        global ans
        temp = 0
        for keys in arr:
            for key in keys:
                if key not in visited:
                    break
            else:
                temp += 1
        ans = max(ans, temp)
    
    else:
        for i in range(next, N*2):
            if not visited[i]:
                visited[i] = i + 1
                dfs(cnt+1, i+1)
                visited[i] = 0


N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

visited = [0] * (N*2)

ans = 0

dfs(0, 0)

print(ans)