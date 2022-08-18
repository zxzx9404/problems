def len(list):   # len 구현
    cnt = 0
    for _ in list:
        cnt += 1
    return cnt

def bfs(v):      # bfs 재귀 구현
    visited[v] = 1
    for w in adjlist[v]:
        if visited[w] == 0:
            bfs(w)


for _ in range(10):
    tc, L = map(int, input().split())
    visited = [0]*100                      # 문제의 조건에 따라 100개의 인덱스
    adjlist = [[] for _ in range(100)]
    arr = list(map(int, input().split()))
    
    for i in range(0, len(arr), 2):        # 경로를 2개씩 끊어서 재가공
        a, b = arr[i], arr[i+1]
        adjlist[a].append(b)               # 단방향이므로 한쪽에만 저장
    bfs(0)
    if visited[99] == 1:                   # 출발지(0번 인덱스)에서 함수 실행
        print(f'#{tc} 1')                  # 목적지(99번 인덱스)에 방문한적이 있으면 경로 있다는 뜻
    else:
        print(f'#{tc} 0')