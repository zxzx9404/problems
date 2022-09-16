# BFS를 이용한 풀이, Python으로는 시간초과 PyPy로는 1860ms

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    adjlist = [[]*N for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        adjlist[a-1].append(b-1)
        adjlist[b-1].append(a-1)
        
    ans = 10000000000000000000
    
    for i in range(N):
        visited = [0]*N
        q = [i]
        visited[i] = 1
        cnt = 0
        while q:
            v = q.pop(0)
            for w in adjlist[v]:
                if visited[w] == 0:
                    visited[w] = visited[v] + 1
                    cnt += 1
                    q.append(w)
        if all(visited):
            ans = min(ans, cnt)
    print(ans)
    
    
# 이왜답? Python 180ms

import sys
input = sys.stdin.readline

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    adjlist = [[]*N for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
    print(N-1)
    

# DFS를 이용한 풀이 / Python 232ms

import sys
input = sys.stdin.readline

def dfs(v, cnt):
    visited[v] = 1
    
    for w in adjlist[v]:
        if visited[w] == 0:
            cnt = dfs(w, cnt+1)
            
    return cnt

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    
    adjlist = [[] for _ in range(N+1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        adjlist[a].append(b)
        adjlist[b].append(a)
    
    visited = [0] * (N+1)
    
    print(dfs(1, 0))
    
    