TC = int(input())

def change(lst, i, j, x):
    global cnt
    for k in range(4): # 인접한 1이 아닌 모든 칸을 2로 바꿈
        if 0 <= i+dy[k] < x and 0 <= j+dx[k] < x and lst[i+dy[k]][j+dx[k]] != 1 and lst[i+dy[k]][j+dx[k]] != 2:
            lst[i+dy[k]][j+dx[k]] = 2
            change(lst, i+dy[k], j+dx[k], x)
    
dx = [1, -1, 0, 0] # 델타 방위
dy = [0, 0, -1, 1]

for tc in range(1, TC+1):
    n = int(input())
    arr = []
    for _ in range(n):
        a = input()
        temp = []
        # 인풋을 숫자 형태로 변환하여 2차원 배열로 저장
        for num in a:
            temp.append(int(num))
        arr.append(temp)
    # 시작점과 도착점 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                goal = [i, j]
            elif arr[i][j] == 2:
                start = [i, j]
    change(arr, start[0], start[1], n) # 시작점을 기준으로 탐색

    if arr[goal[0]][goal[1]] == 2: # 시작점에서 출발하여 연결된 모든 점을 2로 바꾸었으므로
        print(f'#{tc} 1')          # 시작점과 도착점이 이어져있다면 도착점의 값이 2로 바뀌었을 것
    else:
        print(f'#{tc} 0')          # 아니라면 이어지지 않음