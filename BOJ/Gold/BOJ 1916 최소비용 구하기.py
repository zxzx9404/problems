# 힙큐를 쓰는 이유가 뭐지..?
# 현재값이 작은것부터 탐색을 하려고 그런건가

import heapq
import sys
input = sys.stdin.readline

N, M = int(input()), int(input())

adjlist = [[] for _ in range(N+1)]
visited = [10**10] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    adjlist[a].append((c, b))

st, ed = map(int, input().split())

q = []
visited[st] = 0
heapq.heappush(q, (0, st))

while q:
    now, v = heapq.heappop(q)
    
    # 현재 v 칸 까지의 최소비용보다 현재 비용이 더 크다면 패스
    if visited[v] < now:
        continue
        
    for c, w in adjlist[v]:
        if now + c < visited[w]:
            visited[w] = now + c
            # 작은걸 먼저 봐야 효율적일 확률이 높아서 heapq를 쓰는듯?
            heapq.heappush(q, (now+c, w))

print(visited[ed])

------

# 맞는것같긴 한데 시간초과..

from collections import deque
import sys
input = sys.stdin.readline

N, M = int(input()), int(input())

adjlist = [[] for _ in range(N+1)]
visited = [10**10] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    adjlist[a].append((b, c))

st, ed = map(int, input().split())

q = deque([st])
visited[st] = 0

while q:
    v = q.popleft()
    
    if visited[v] 
    
    for w, c in adjlist[v]:
        if visited[v] + c < visited[w]:
            visited[w] = visited[v] + c
            q.append(w)

print(visited[ed])