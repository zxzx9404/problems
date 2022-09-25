def f(temp, cnt):
    if cnt == M:
        print(*temp)
        return
    
    for j in range(N):
        f(temp + [arr[j]], cnt+1)
            

N, M = map(int, input().split())

arr = list(range(1, N+1))
visited = [0] * N

f([], 0)