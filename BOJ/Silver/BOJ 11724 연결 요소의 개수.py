# 실행 시간 : 788ms

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adjlist = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        q = deque()
        q.append(i)
        while q:
            x = q.popleft()
            for w in adjlist[x]:
                if visited[w] == 0:
                    q.append(w)
                    visited[w] = 1
        cnt += 1
        
print(cnt)