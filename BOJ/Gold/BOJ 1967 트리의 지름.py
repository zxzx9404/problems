import sys
sys.setrecursionlimit(10000)

def dfs(c, temp):
    global ans
    for w, r in adjlist[c]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w, temp + r)
            visited[w] = 0

    ans = max(ans, temp)

N = int(input())

adjlist = [[] for _ in range(N+1)]
chr = [[] for _ in range(N+1)]

visited = [0] * (N+1)


for _ in range(N-1):
    a, b, c = map(int, input().split())
    chr[a].append((b, c))
    adjlist[a].append((b, c))
    adjlist[b].append((a, c))

ans = 0

for i in range(1, N+1):
    if not chr[i]:
        visited[i] = 1
        dfs(i, 0)

print(ans)

##################
'''
import sys
sys.setrecursionlimit(10000)

def up(c, temp):
    if par[c] and not visited[par[c][0]]:
        visited[par[c][0]] = 1
        up(par[c][0], temp + par[c][1])
        visited[par[c][0]] = 0

    if chr[c]:
        for i in range(len(chr[c])):
            if not visited[chr[c][i][0]]:
                visited[chr[c][i][0]] = 1
                down(chr[c][i][0], temp + chr[c][i][1])
                visited[chr[c][i][0]] = 0
    
    if sum(visited) == N:
        global ans
        ans = max(ans, temp)

def down(c, temp):
    if chr[c]:
        for i in range(len(chr[c])):
            if not visited[chr[c][i][0]]:
                visited[chr[c][i][0]] = 1
                down(chr[c][i][0], temp + chr[c][i][1])
                visited[chr[c][i][0]] = 0
    else:
        global ans
        ans = max(ans, temp)

N = int(input())

chr = [[] for _ in range(N+1)]
par = [0]*(N+1)
visited = [0] * (N+1)

for _ in range(N-1):
    a, b, c = map(int, input().split())
    chr[a].append((b, c))
    par[b] = ((a, c))

ans = 0
for i in range(1, N+1):
    if not chr[i]:
        visited[i] = 1
        up(i, 0)

print(ans)
'''