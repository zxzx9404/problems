import copy

def shark(shark_i, shark_j, shark_dir, temp, fishes, arr):
    for t in range(1, 17):
        if fishes[t]:  # 물고기가 살아있다면
            i, j, dir = fishes[t]
            for k in range(8):  # 아무튼 8방향 보면서 이동
                k = (k + dir) % 8
                ni, nj = i + delta[k][0], j + delta[k][1]
                if 0 <= ni < 4 and 0 <= nj < 4 and (ni != shark_i or nj != shark_j):
                    change = arr[ni][nj]
                    if change:  # 갈 자리에 물고기 있으면 서로 바꿔줌
                        fishes[change][0], fishes[change][1] = i, j
                    fishes[t][0], fishes[t][1], fishes[t][2] = ni, nj, k
                    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                    break

    for k in range(1, 4):  # 상어 이동 파트
        ni, nj = shark_i + delta[shark_dir][0]*k, shark_j + delta[shark_dir][1]*k
        if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj]:
            eat_fish = arr[ni][nj]  # 뭔가 복잡해 보이지만 그냥 재귀 쏘기 전에 물고기 먹은 처리 해주고, 재귀식 끝나면 다시 물고기 살려놓기(?)임
            next_i, next_j, next_dir = fishes[eat_fish]
            fishes[eat_fish], arr[ni][nj] = 0, 0
            shark(next_i, next_j, next_dir, temp + eat_fish, copy.deepcopy(fishes), copy.deepcopy(arr))
            arr[ni][nj] = eat_fish
            fishes[eat_fish] = [next_i, next_j, next_dir]
            
    global ans
    ans = max(ans, temp)
    return


delta = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
fishes = [[] for _ in range(17)] # 물고기번호 = 인덱스 번호 // 저장 값은 좌표와 방향
arr = [[[] for _ in range(4)] for _ in range(4)] # 실제 보드판 // 저장 값은 물고기 번호

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = temp[j*2]
        fishes[temp[j*2]] = [i, j, temp[j*2+1]-1]

ans = arr[0][0]
shark_dir = fishes[ans][2]
fishes[ans] = []
arr[0][0] = 0

shark(0, 0, shark_dir, ans, fishes, arr)
print(ans)