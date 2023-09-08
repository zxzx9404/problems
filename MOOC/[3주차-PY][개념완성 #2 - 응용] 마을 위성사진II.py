import sys


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_lake = [list(map(int, readl().rstrip())) for r in range(N)]
	return N, map_lake


sol = 0
# 입력 받는 부분
N, map_lake = Input_Data()

# 여기서부터 작성
def check_lake(st_i, st_j):
    arr = [(st_i, st_j)]
    
    while arr:
        i, j = arr.pop()
        
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and map_lake[ni][nj] and not visited[ni][nj]:
                arr.append((ni, nj))
                visited[ni][nj] = 1
            

visited = [[0] * N for _ in range(N)]
di = [1, 1, 1, -1, -1, -1, 0, 0]
dj = [1, -1, 0, 1, -1, 0, 1, -1]

for i in range(N):
    for j in range(N):
        if map_lake[i][j] and not visited[i][j]:
            sol += 1
            visited[i][j] = 1
            check_lake(i, j)

# 출력하는 부분
print(sol)
