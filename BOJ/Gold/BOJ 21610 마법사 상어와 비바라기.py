N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
delta = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for _ in range(M):
    d, s = map(int, input().split())  # 방향, 이동 거리
    next_cloud = []  # 구름의 최종 위치
    
    for i, j in cloud:  # 구름 움직이기
        ni = (N + i + delta[d][0] * s) % N
        nj = (N + j + delta[d][1] * s) % N
        next_cloud.append([ni, nj])
    
    
    visited = [[0]*N for _ in range(N)]
        
    for i, j in next_cloud:  # 구름 위치에 물 +1
        arr[i][j] += 1
        visited[i][j] = 1  # 다음 구름이 생길 수 없으므로 방문처리

    
    for i, j in next_cloud:  # 물복사 버그
        for di, dj in diagonal:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                arr[i][j] += 1
                
    cloud = []
    for i in range(N):  # 새로운 구름 생성
        for j in range(N):
            if arr[i][j] >= 2 and not visited[i][j]:
                cloud.append([i, j])
                arr[i][j] -= 2

print(sum(sum(arr, [])))