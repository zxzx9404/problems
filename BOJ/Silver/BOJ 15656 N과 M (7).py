def f(temp, cnt):
    if cnt == m:
        print(*temp)
        return
        
    for i in range(n):
        f(temp + [arr[i]], cnt+1)


n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))

f([], 0)