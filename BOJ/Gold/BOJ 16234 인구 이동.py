# Python3 : 6036ms, PyPy3 : 1160ms
'''
1. arr를 순회하며 자신과 연합이 될 수 있는 모든 국가를 찾는다.
2. 본인을 포함한 연합 국가가 2개 이상인 경우 해당 (국가들의 합 // 국가의 수)를 구함
3. 연합이 될 국가의 좌표를 담아둔 리스트를 순회하며 새로운 인구 값을 넣어줌
4. 이미 방문한 국가는 visited = True로 체크하여 한 사이클에서는 한번의 연합만 가능하게 함
5. 연합이 발생하지 않는다면 ans 출력
'''

def population_move():
    temp = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                temp += check_union(i, j)
    return temp


def check_union(i, j):
    visited[i][j] = True
    q = [(i, j)]
    union = [(i, j)]

    sum_population = arr[i][j]
    sum_count = 1

    while q:
        i, j = q.pop()

        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(arr[i][j]-arr[ni][nj]) <= R:
                visited[ni][nj] = True
                q.append((ni, nj))
                union.append((ni, nj))
                sum_population += arr[ni][nj]
                sum_count += 1

    if sum_count > 1:
        avg_population = sum_population // sum_count
        for i, j in union:
            arr[i][j] = avg_population
        return 1
    return 0


N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

ans = 0
while population_move():
    visited = [[False] * N for _ in range(N)]
    ans += 1

print(ans)