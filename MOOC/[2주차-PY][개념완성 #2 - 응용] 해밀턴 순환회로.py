# 문제를 꼼꼼히 읽자..
# 이동기 불가능한 항공은 0이다.

import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [list(map(int, readl().split())) for _ in range(N)]
	return N, matrix



# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성


def dfs(c, now, fee):
    global sol
    if fee >= sol:
        return
    
    if c == N-1 and matrix[now][0]:
        sol = min(sol, fee + matrix[now][0])
        return

    for i in range(1, N):
        if not visited[i] and matrix[now][i]:
            visited[i] = 1
            dfs(c+1, i, fee + matrix[now][i])
            visited[i] = 0

sol = 1200
visited = [0] * N
dfs(0, 0, 0)


# 출력하는 부분
print(sol)
