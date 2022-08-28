def dfs(s):
    v = s
    visited_d[v] = 1
    ans_d.append(v)
    for w in adjlist[v]:
        if visited_d[w] == 0:
            dfs(w)


def bfs(s):
    visited_b = [0]*N
    q = [s]
    visited_b[s] = 1
    ans_b.append(s)
    while q:
        v = q.pop(0)
        for w in adjlist[v]:
            if visited_b[w] == 0:
                q.append(w)
                visited_b[w] = 1
                ans_b.append(w)
                

V, E, s = map(int, input().split())

N = V+1

adjlist = [[] for _ in range(N)]
ans_d, ans_b = [], []
arr = []
for _ in range(E):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

for i in adjlist:
    i.sort()

visited_d = [0]*N
dfs(s)
bfs(s)

print(*ans_d)
print(*ans_b)