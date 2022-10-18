### 풀이 과정 ###
# 1. 최초에 arr를 순회하면서 치즈(1)인 부분을 찾아서 좌표 저장
# 2. 0인 곳을 발견했다면, 바깥 공기인지, 치즈 내부 구멍인지 구분
#     - 바깥(치즈를 녹일수 있는)이라면 out_sides에 좌표 추가
#     - 내부 구멍이라면, in_sides에 구멍 단위로 추가(차후 치즈가 녹은 뒤에 다시 확인해야 함)
# 3. 치즈의 좌표들을 순회하면서 바깥 공기와 맞닿아 있다면 녹임
# 4. 한 타임동안 녹을 치즈가 다 녹고 난 뒤, 치즈 내 구멍들(in_sides)을 순회하며 공기와 맞닿게 되었는지 확인
# 5. 맞닿았다면 in_sides에서 제거한 뒤, out_sides에 추가
# 6. 치즈가 모두 녹았다면 직전 치즈의 양을 저장한 채로 반복문 탈출 후 출력


def first_check(i, j):
    flag = False
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    
    temp = [(i, j)]
    q = [(i, j)]
    
    while q:
        i, j = q.pop()
        
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
        
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 0:
                q.append((ni, nj))
                temp.append((ni, nj))
                visited[ni][nj] = 1

                if ni == 0 or ni == N-1 or nj == 0 or nj == M-1:
                    flag = True
    
    if flag:
        out_sides.extend(temp)
    else:
        in_sides.append(temp)
    

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cheese = []
out_sides, in_sides = [], []
t = 0
ex_cheese = 0

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            cheese.append((i, j))
        else:
            if (i, j) not in out_sides:
                if in_sides:
                    for k in in_sides:
                        if (i, j) in k:
                            break
                    else:
                        first_check(i, j)
                else:
                    first_check(i, j)

while cheese:
    t += 1
    ex_cheese = len(cheese)
    temp = []
    idx = 0
    
    while idx < len(cheese):
        i, j = cheese[idx][0], cheese[idx][1]
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if (ni, nj) in out_sides:
                temp.append(cheese.pop(idx))
                break
        else:
            idx += 1
    
    if not cheese:
        break
    
    else:
        out_sides.extend(temp)
        
        if in_sides:
            idx = 0
            while idx < len(in_sides):
                p = False
                for i, j in in_sides[idx]:
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = i + di, j + dj
                        if (ni, nj) in out_sides:
                            out_sides.extend(in_sides.pop(idx))
                            p = True
                            break
                    if p:
                        break
                else:
                    idx += 1    

print(t)
print(ex_cheese)