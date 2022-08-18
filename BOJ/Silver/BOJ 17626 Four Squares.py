# 브루트포스 풀이
# range를 역순으로 쓸때는 범위를 한번 더 살피자
n = int(input())

ans = 4

for i in range(int(n**0.5), 0, -1):
    if n == i**2:
        ans = 1
        break
    else:
        a = n - i**2
        for j in range(int(a**0.5), 0, -1):
            if a == j**2:
                ans = min(ans, 2)
            else:
                b = a - j**2
                for k in range(int(b**0.5), 0, -1):
                    if b == k**2:
                        ans = min(ans, 3)

print(ans)

# dp 풀이

# N = int(input())
# dp = [0,1]

# for i in range(2, N+1):
#     min_value = 1e9
#     j = 1

#     while (j**2) <= i:
#         min_value = min(min_value, dp[i - (j**2)])
#         j += 1

#     dp.append(min_value + 1)
# print(dp[N])