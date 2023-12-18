from collections import defaultdict
import heapq
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dijk(st):
    visited = [int(1e9)]*(n+1)
    visited[st] = 0
    visited[0] = 0
    FROM = [[] for _ in range(n+1)]
    hq = []
    heapq.heappush(hq, [0, st])
    while hq:
        sum_cost, now = heapq.heappop(hq)
        if visited[now] < sum_cost:
            continue
        
        for next, cost in nodes[now]:
            new_cost = sum_cost + cost
            if visited[next] > new_cost:
                visited[next] = new_cost
                FROM[next] = [now]
                heapq.heappush(hq, [new_cost, next])
            elif visited[next] == new_cost:
                FROM[next].append(now)
    return FROM

def DFS(num):
    global flag
    if not num or flag:
        return
    for k in FROM[num]:
        if [k, num] in ghhg:
            flag = True
            return
        else: DFS(k)

TC = int(input())
for tc in range(TC):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    nodes = defaultdict(list)
    ghhg = [[g, h], [h, g]]

    for _ in range(m):
        a, b, d = map(int, input().split())
        nodes[a].append([b, d])
        nodes[b].append([a, d])
        
    dest = [int(input()) for _ in range(t)]
    dest.sort()
    
    FROM = dijk(s)
    # print(FROM)
    ans = []
    for i in dest:
        flag = False
        DFS(i)
        if flag:
            ans.append(i)
    print(*ans)
