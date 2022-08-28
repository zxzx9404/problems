def bfs(i):
    # i를 초기값으로 가지는 q 생성
    q = [i]
    visited[i] = 1
    while q:
        idx = q.pop(0)
        for w in adjlist[idx]:
            # idx칸의 인접 리스트에 방문하지 않은 노드가 있다면
            if visited[w] == 0:
                # 큐에 넣어줌
                q.append(w)
                # visited list에 노드를 지난 횟수를 표시하기 위해 +1
                visited[w] = visited[idx] + 1

TC = int(input())

for tc in range(1, TC+1):
    V, E = map(int, input().split())
    N = V + 1
    # 인접 리스트 만들기
    adjlist = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjlist[a].append(b)
        adjlist[b].append(a)
    # visited list 만들기
    visited = [ 0 for _ in range(N)]
    s, g = map(int, input().split())
    # 출발점을 기준으로 bfs 실행
    bfs(s)
    # g 노드에 방문하지 못했다면 0 출력
    if visited[g] == 0:
        print(f'#{tc} 0')
    # 방문했다면 도착까지의 이동수 - 초기 값(1) 출력
    else:
        print(f'#{tc} {visited[g]-1}')