from collections import deque
import sys
input = sys.stdin.readline

# 먹을수 있는 물고기를 탐색하는 BFS
def bfs(i, j):
    global change, size, ans, temp, eat
    q = deque()
    # 먹을수 있는 물고기 목록이 담길 리스트
    can_eat = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        y, x = q.popleft()
        # 한번의 탐색 이후 다시 visited를 0으로 돌려주기 위한 좌표 저장
        change.append((y, x))
        # 4방향 델타 탐색
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = y + di, x + dj
            # 좌표 내에 존재하는 점이며, 방문한적 없고, 아기 상어보다 크지 않은 물고기가 있을 경우
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] <= size:
                # 방문 처리
                visited[ni][nj] = visited[y][x] + 1
                # 방문한 물고기가 먹을 수 있는 물고기라면
                if arr[ni][nj] < size and arr[ni][nj] != 0 and temp == n*n:
                    # 해당 물고기 까지의 거리 저장
                    temp = visited[ni][nj]
                    # 먹을수 있는 물고기 리스트에 좌표 저장
                    can_eat.append((ni, nj))
                # 같은 거리에 있는 다른 먹을수 있는 물고기일 경우
                elif visited[ni][nj] == temp and arr[ni][nj] < size and arr[ni][nj] != 0:
                    # 좌표 저장
                    can_eat.append((ni, nj))
                # 먹을수 있는 물고기보다 더 멀경우 추가 탐색 X
                if visited[ni][nj] > temp:
                    change.append((ni, nj))
                else:
                    q.append((ni, nj))
    # 먹을수 있는 물고기가 없을 경우 False 리턴
    if len(can_eat) == 0:
        return 0
    else:
        # 먹으러 이동해야 하는 칸수만큼 정답 늘려주기
        ans += (temp - 1)
        # visited 초기화 및 상어 위치 초기화
        visited[i][j] = 0
        arr[i][j] = 0
        while change:
            y, x = change.pop()
            visited[y][x] = 0
        # 먹을수 있는 물고기 리스트를 반환
        return can_eat


def eat_fish(can_eat):
    global size, eat
    # 동일 거리면 위면서, 왼쪽이므로 y좌표값이 작은 것, 같다면 x 좌표값이 작은것을 먹는다는 뜻
    ans_i, ans_j = n, n
    for y, x in can_eat:
        # y좌표가 더 작다면
        if y < ans_i:
            # 먹을 물고기로 저장
            ans_i, ans_j = y, x
        # y는 같고 x가 더 작다면
        elif y == ans_i:
            # 먹을 물고기로 저장
            if x < ans_j:
                ans_i, ans_j = y, x
    # 상어를 먹은 물고기 위치로 이동
    arr[ans_i][ans_j] = 9
    # 사이즈업을 위한 카운팅
    eat += 1
    if eat == size:
        eat = 0
        size += 1
    # 새로운 상어의 위치 반환
    return ans_i, ans_j


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
size = 2
eat = 0
change = deque()
ans = 0

# 상어의 최초 위치 찾기
p = False
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sti, stj = i, j
            p = True
            break
    if p:
        break


while True:
    # 임시 거리값을 최대로 초기화
    temp = n*n
    # 상어의 초기 좌표로 BFS 탐색 시작
    c = bfs(sti, stj)
    # 먹을수 있는 물고기가 있다면
    if c:
        # 최종적으로 먹을 물고기를 정한 뒤, 해당 위치로 상어를 옮겨 재탐색 시작
        sti, stj = eat_fish(c) 
    else:
        # 없다면 break
        break
# 총 이동 칸수 출력
print(ans)