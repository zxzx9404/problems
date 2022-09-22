n, m = map(int, input().split())

arr = []

def dfs(st):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(st, n+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()
dfs(1)