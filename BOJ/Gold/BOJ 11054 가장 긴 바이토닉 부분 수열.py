N = int(input())
arr = list(map(int, input().split()))
ascending_dp = [1]*N
descending_dp = [1]*N


# 앞에서부터 본인까지 제일 긴 오름차순 수열 구하기 // (1, 2, 5, 2, 1)에서 1, 2, 5를 구함
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            ascending_dp[i] = max(ascending_dp[i], ascending_dp[j]+1)

# 뒤에서부터 본인까지 제일 긴 오름차순 수열 구하기 // (1, 2, 5, 2, 1)에서 5, 2, 1을 구함
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            descending_dp[i] = max(descending_dp[i], descending_dp[j]+1)


dp = [0]*N

# 둘이 합치고 중복된 곳 -1 해주기 // 위의 예시에선 5가 두번 계산됨
for i in range(N):
    dp[i] = ascending_dp[i]+descending_dp[i] - 1

print(max(dp))