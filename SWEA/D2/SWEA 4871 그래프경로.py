def bfs(v):                                     # 재귀를 통한 bfs 구현
    visited[v] = 1
    for w in adjlist[v]:
        if visited[w] == 0:
            bfs(w)



TC = int(input())

for tc in range(1, TC+1):
    V, E = map(int, input().split())
    
    visited = [0]*V
    adjlist = [[] for _ in range(V)]
    for i in range(E):
        a, b = map(int, input().split())        # 문제에 단방향에 대한 언급은 없었지만,
        adjlist[a-1].append(b-1)                # 그림상 단방향처럼 보여서 단방향으로 설정
    s, e = map(int, input().split())            
    bfs(s-1)
    if visited[s-1] == 1 and visited[e-1] == 1: # s와 e가 이어져있으면, 모두 방문했어야 하므로 둘다 1이 나와야 함
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')