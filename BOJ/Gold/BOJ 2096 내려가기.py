# 메모리를 신경써야 함 -> 매번 갱신하는 방식으로 해결

from sys import stdin
input = stdin.readline

N = int(input())
dp = list(map(int, input().split()))
max_dp = dp
min_dp = dp

for _ in range(N-1):
    a, b, c = map(int, input().split())
    max_dp = [a + max(max_dp[:2]),  b + max(max_dp), c + max(max_dp[1:])]
    min_dp = [a + min(min_dp[:2]),  b + min(min_dp), c + min(min_dp[1:])]

print(max(max_dp), min(min_dp))
