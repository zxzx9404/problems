# 재귀 문제인줄 알았더니 개수보니 재귀로 푸는게 아니었군
# dp 문제
# 한 동전으로 만들수 있는 가짓수를 모두 구하고, 다른 동전으로 계속 경우의 수 추가하면서 엎어가는 방식

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, target+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[target])