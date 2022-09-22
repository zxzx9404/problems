for tc in range(1, 11):
    n, st = map(int, input().split())
    arr = list(map(int, input().split()))
    # 인접 리스트와 visited 생성
    adjlist = [[] for _ in range(max(arr)+1)]
    visited = [0] * (max(arr)+1)
    for i in range(n//2):
        adjlist[arr[i*2]].append(arr[i*2+1])
    
    # BFS 탐색
    q = [st]
    while q:
        v = q.pop(0)
        for w in adjlist[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                q.append(w)
                
    # 가장 늦게 연락받은 사람을 찾는 과정
    late = 0
    ans = 0
    for i in range(max(arr)):
        if late <= visited[i]:
            late = visited[i]
            ans = i
    print(f'#{tc} {ans}')