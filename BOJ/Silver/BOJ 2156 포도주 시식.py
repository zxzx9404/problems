# 포도주 1만잔 먹다간 죽겠다..
# 500ms

N = int(input())
wine = [int(input()) for _ in range(N)]
dp = [0]*N
dp[0] = wine[0]
if N >= 2:
    dp[1] = wine[0]+wine[1]

for i in range(2, N):
                # XOO                            # OXO             # OOX
    dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i], dp[i-1])

print(dp[N-1])



#### 해설 ####

'''
3잔을 기준으로 잡았을 때 각 잔을 먹거나 / 안먹는다면

XXX
OXX
XOX
XXO
OOX
OXO
XOO
OOO

다음과 같은 8가지 경우의 수가 발생하고 이를 4가지 케이스로 분류할 수 있음

case1) OOX, XOX, OXX, XXX

case2) OXO, XXO

case3) XOO

case4) OOO

case1의 경우 마지막 잔을 먹지 않는 경우이기 때문에 나머지 두 잔을 먹는 OOX가 반드시 최대값임
case2의 경우 두번째, 세번째 잔이 동일하므로 OXO가 반드시 최대값임
case3은 봐야 함
case4는 문제의 조건(3잔 스트레이트 안됨)에 의해 불가능

즉, OOX, OXO, XOO 이 3가지의 경우의 수만 비교해 나가면서 계산하면 된다.
'''