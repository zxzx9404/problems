N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

ans = 1

for i in range(N-1):
    for j in range(M-1):
        for k in range(1, min(M-j, N-i)):
            if arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]:
                ans = max(ans, k+1)
print(ans**2)