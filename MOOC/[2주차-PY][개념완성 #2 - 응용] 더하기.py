# 큰 숫자부터 계산해나가야 연산 횟수를 줄일 수 있다!

def dfs(c, now):
    global flag
     
    if now == K:
        flag = True
        return
    
    if c < 0:
        return
     
    if flag:
        return
     
    
    dfs(c-1, now)
    dfs(c-1, now + nums[c])
 
TC = int(input())
 
for _ in range(TC):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    flag = False

    dfs(N-1, 0)
    
    if flag:
        print('YES')
    else:
        print('NO')
