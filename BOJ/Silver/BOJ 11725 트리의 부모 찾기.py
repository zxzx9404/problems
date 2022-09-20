from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)


def dfs(v):
    for w in adjlist[v]:
        # 탑다운 방식으로 탐색하므로, w의 부모가 v
        if par[w] == 0:
            par[w] = v
            dfs(w)


n = int(input())

adjlist = deque(deque() for _ in range(n+1))
par = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

# 루트부터 뻗어나감
dfs(1)

for i in range(2, n+1):
    print(par[i])
