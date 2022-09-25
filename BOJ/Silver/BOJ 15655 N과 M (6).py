def f(temp, cnt):
    if cnt == m:
        if sorted(temp) not in ans:
            ans.append(sorted(temp))
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            f(temp + [arr[i]], cnt+1)
            visited[i] = 0


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * n

ans = []
f([], 0)

for j in ans:
    print(*j)