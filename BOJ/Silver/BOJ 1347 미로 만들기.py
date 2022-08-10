N = int(input()) # 자료 받기
walk = input()

x_y = [[0, 0]] # 좌표값 측정을 위한 초기 좌표 0,0 설정
dx = [-1, 0, 1, 0] # 델타 탐색
dy = [0, 1, 0, -1]
dir = 2 # 1~4 방위는 우 하 좌 상 순
for i in walk:
    if i == 'R':
        dir = (dir + 1) % 4
    elif i == 'L':
        if dir != 0:
            dir -= 1
        else:
            dir = 3
    else: # 이동 후의 좌표를 추가
        x = x_y[-1][0] + dx[dir]
        y = x_y[-1][1] + dy[dir]
        x_y.append([x, y])
        
x_y = sorted(x_y, key=lambda x: x[0]) # 필요한 x축의 길이를 위해 sort
x_min, x_max = x_y[0][0], x_y[-1][0]
x_y = sorted(x_y, key=lambda x: x[1]) # 필요한 y축의 길이를 위해 sort
y_min, y_max = x_y[0][1], x_y[-1][1]

miro =[] # real 미로
for _ in range(x_min, x_max+1): # 일단 모두 #으로
    miro.append(['#']*(y_max-y_min+1))

for i in range(len(x_y)): # 음수 나오면 양수전환용
    x_y[i] = (x_y[i][0] - x_min, x_y[i][1] - y_min)

for i, j in x_y: # 해당하는곳에 점
    miro[i][j] = '.'

for q in miro: # 출력
    print(''.join(q))
        