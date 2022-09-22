import sys
sys.setrecursionlimit(1000000)

# 일반적인 bfs 탐색 알고리즘
def bfs_normal():
    global visited
    cnt = 0
    # visited list 생성
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 방문하지 않은 경우, 해당 색을 기준으로 4방향 델타 탐색
            if visited[i][j] == 0:
                visited[i][j] = 1
                # 한 구역이 새로 등장한 것이므로 +1
                cnt += 1
                delta(i, j, n, arr[i][j])

    return cnt

# 적록색약의 경우
def bfs_jeokrok():
    # 그냥 G를 모두 R로 바꿔준 후에
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'G':
                arr[i][j] = 'R'
    # 윗 방식과 동일하게 탐색
    return bfs_normal()


# 델타 탐색 함수
def delta(i, j, n, color):
    for di, dj, in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + di, j + dj
        # 범위 안에 있으면서, 컬러가 일치하면서, 방문하지 않았을 경우 방문으로 바꿈
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == color and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            # 해당 점을 기준으로 다시 4방위 델타
            delta(ni, nj, n, color)

n = int(input())
arr = []
# 적록색약 탐색 시 G를 R로 변경할 것이므로,
# 문자열을 1개씩 슬라이싱 해서 받아야 함
for i in range(n):
    a = input()
    temp = []
    for j in a:
        temp.append(j)
    arr.append(temp)

print(bfs_normal(), bfs_jeokrok())