mel_num = int(input())
len_big = 0 #큰 면적의 밭의 가로
hei_big = 0 #큰 밭의 면적 세로
real_bat = 0 #실제 밭의 면적
small_bat = [] # ㄱ ㄴ 형태에서 비어있는 가상의 밭
bat = [] #입력 자료

#자료 인풋받기
for i in range(6):
    a = b = 0
    a, b = map(int, input().split())
    bat.append([a, b])

#큰 밭의 면적 구하기
for i in range(6):
    if bat[i][0] == 1:
        len_big += bat[i][1]
for i in range(6):
    if bat[i][0] == 3:
        hei_big += bat[i][1]

#작은 밭의 면적 구하기
if bat[0][0] == bat[4][0]:
    small_bat.append(bat[5][1])
if bat[5][0] == bat[1][0]:
    small_bat.append(bat[0][1])

for i in range(4):
    if bat[i][0] == bat[i+2][0]:
        small_bat.append(bat[i+1][1])

real_bat = (len_big*hei_big) - (small_bat[0]*small_bat[1])

print(real_bat*mel_num)

