### 풀이 아이디어 ###
'''
2차원으로 arr를 받지만, 사실 2차원 좌표 arr[i][j]가 의미하는 것이
i -> j 의 이동 비용일 뿐, 모든 점이 연결된 1차원 방문탐색을 하는것과 같다.
고로 1차원 visited를 만들고, 0번 인덱스(사무실)을 제외한 모든 곳을 방문한 뒤
사무실로 돌아올때까지의 배터리 사용량을 모두 더해서 최솟값을 찾는다.
'''


# DFS 방식 풀이
def dfs(i, j):
    global temp, ans

    # 방문 처리
    visited[j] = 1
    # 방문하는데 드는 배터리 사용량 더해줌
    temp += arr[i][j]

    if all(visited):
        # 전부 방문했을 경우, 마지막 점에서 돌아오는 배터리 사용량 더해줌
        a = temp + arr[j][0]
        ans = min(ans, a)
        return

    # 아직 방문하지 않은 곳이 있고, 같은 점이 아닐 경우
    for k in range(1, n):
        if visited[k] == 0 and j != k:
            dfs(j, k)
            # 재귀 후에는 해당 값 빼주고, 방문처리 지우기
            visited[k] = 0
            temp -= arr[j][k]


TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    visited[0] = 1
    ans = 100000000000
    temp = 0
    for i in range(1, n):
        dfs(0, i)
        # 재귀식 탈출 후에는 방문처리 지우고, 사용량 뺴주기
        temp -= arr[0][i]
        visited[i] = 0

    print(f'#{tc} {ans}')