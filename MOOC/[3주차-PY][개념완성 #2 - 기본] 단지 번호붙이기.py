import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_apt = [list(map(int,list(readl().strip()))) for r in range(N)]
	return N, map_apt

cnt = 0
list_size = []

# 입력 받는 부분
N, map_apt = Input_Data()

# 여기서부터 작성
def check_apt(st_i, st_j):
    arr = [[st_i, st_j]]
    cnt = 1
    
    while arr:
        i, j = arr.pop()
        
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            
            if 0 <= ni < N and 0 <= nj < N and map_apt[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                cnt += 1
                arr.append((ni, nj))
        
    return cnt
    

visited = [[0]*N for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for i in range(N):
    for j in range(N):
        if map_apt[i][j] and not visited[i][j]:
            visited[i][j] = 1
            num = check_apt(i, j)
            cnt += 1
            list_size.append(num)

list_size.sort()

# 출력하는 부분
print(cnt)
print(*list_size,sep='\n')
