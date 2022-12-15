# 36ms / 백트래킹 문제

def dfs(n, sour, bitter):
    global ans
    
    if n == N:
        if bitter:
            ans = min(ans, abs(sour - bitter))
        return
    
    # n번째 재료를 사용하지 않음
    dfs(n + 1, sour, bitter)
    # n번째 재료를 사용
    dfs(n + 1, sour * arr[n][0], bitter + arr[n][1])


N = int(input())
ans = 10**9
arr = [list(map(int, input().split())) for _ in range(N)]

dfs(0, 1, 0)

print(ans)
