# 44ms
# 제곱근까지만 하면 되는거 맞지?

N = int(input())

def dfs(cnt, num):
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return
        
    if cnt == N:
        print(num)
        return
    
    for j in range(1, 10):
        dfs(cnt+1, num*10+j)

for i in (2, 3, 5, 7):
    dfs(1, i)