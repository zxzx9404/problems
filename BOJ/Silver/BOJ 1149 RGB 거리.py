n = int(input())


arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    # i번째 집을 칠할 때의 최소 누적합을 색깔별로 계속 구해나감
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]

print(min(arr[n-1][0], arr[n-1][1], arr[n-1][2]))