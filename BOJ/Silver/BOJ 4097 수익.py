import sys
input = sys.stdin.readline

while True:
    day = int(input())
    
    if not day:
        break
    
    dp = [int(input()) for _ in range(day)]
    
    for i in range(1, day):
        dp[i] = max(dp[i], dp[i-1]+dp[i])
    
    print(max(dp))