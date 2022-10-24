# 84ms
'''
1. 최초에 arr를 순회하며 시작점, 도착점, 물의 위치를 찾아줌
2. 물과 고슴도치는 같은 칸에 있을 수 없으니, 물을 먼저 1회 bfs 돌리고,
3. 고슴도치가 갈 수 있는 길을 1회 bfs 돌린다.
4. 고슴도치가 더 이상 이동할 수 없으면 'KAKTUS' 출력
5. 고슴도치가 비버의 굴에 도착했다면 걸린 시간 출력
'''

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

# 필요한 위치들 찾기
water = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            sti, stj = i, j
        if arr[i][j] == 'D':
            edi, edj = i, j
        if arr[i][j] == '*':
            water.append((i, j))    

time = 0
q = [(sti, stj)]
arr[sti][stj] = 0
while True:
    time += 1
    temp = []
    # 물에 대해 1회 BFS 돌리기
    while water:
        i, j = water.pop()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '.':
                arr[ni][nj] = '*'
                temp.append((ni, nj))
    water = temp
    temp = []
    
    # 고슴도치가 갈 수 있는 곳에 1회 BFS 돌리기
    while q:
        i, j = q.pop()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            # 도착점에 도달했다면 걸린 시간 출력 후 종료
            if ni == edi and nj == edj:
                print(time)
                quit()
            elif 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '.':
                arr[ni][nj] = time
                temp.append((ni, nj))

    # 고슴도치가 더 이상 갈 수 있는 곳이 없다면 KAKTUS 출력 후 종료
    if not temp:
        print('KAKTUS')
        quit()
    q = temp