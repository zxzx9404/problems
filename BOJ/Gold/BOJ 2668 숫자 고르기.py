def dfs(up):
    down = arr[up]
    if not visited[down]:
        visited[down] = 1
        first.add(up), second.add(down)
        dfs(down)
    

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]
ans = []
visited = [0] * (N+1)

for i in range(1, N+1):
    first, second = set(), set()
    dfs(i)
    
    if first == second:
        ans.extend(first)
    else:
        for i in second:
            visited[i] = 0

print(len(ans))
for i in sorted(ans):
    print(i)