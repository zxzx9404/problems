# DFS 방식
def dfs(v, temp):
    global ans
    # N점에 도달했으면 값 비교
    if v == N:
        ans = min(ans, temp)
        return
        
    # 이미 현재 최소값보다 크다면 return
    if temp > ans:
        return
    # 방문처리
    visited[v] = 1

    for w in adjlist[v]:
        # 방문하지 않은 인접 노드가 있다면
        if visited[w[0]] == 0:
            # 해당 노드 번호, 노드까지의 이동 거리를 포함해 재귀 호출
            dfs(w[0], temp + w[1])
            # 방문 해제 처리
            visited[w[0]] = 0

TC = int(input())

for tc in range(1, TC+1):
    N, E = map(int, input().split())
    adjlist = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    for _ in range(E):
        a, b, c = map(int, input().split())
        adjlist[a].append((b, c))

    ans = 10**9
    dfs(0, 0)
    print(f'#{tc} {ans}')




