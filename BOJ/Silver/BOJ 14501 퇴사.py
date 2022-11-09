N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)

for i in range(N):
    day, earn = arr[i][0], arr[i][1]
    if i+day <= N:
        for j in range(i+day, N+1):
            dp[j] = max(dp[j], dp[i] + earn)

print(dp[N])

