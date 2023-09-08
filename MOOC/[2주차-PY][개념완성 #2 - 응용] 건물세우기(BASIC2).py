N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
using = [0]*N
ans = 100 * N

def dfs(c, temp):
    global ans
    if temp >= ans: return  # 없으면 시간초과
    
    if c == N:
        if ans > temp:
            ans = temp
        return
    
    for i in range(N):
        if not using[i]:
            using[i] = 1
            dfs(c+1, temp + arr[c][i])
            using[i] = 0


dfs(0, 0)
print(ans)
