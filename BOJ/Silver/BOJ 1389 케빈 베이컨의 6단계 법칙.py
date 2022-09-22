def bfs(o, n):
    visited = [0] * (n+1)
    q = [o]
    visited[o] = 1
    
    while q:
        v = q.pop(0)
        for w in adjlist[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
            
    return sum(visited) - 5


n, m = map(int, input().split())
adjlist = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

min = 10000000

for i in range(1, n+1):
    temp = bfs(i, n)
    if min > temp:
        min = temp
        min_idx = i

print(min_idx)