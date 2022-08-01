#기둥 개수 인풋 및 변수 선언
N = int(input())
x = []
y = []

#자료 인풋
for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    
imsi_max_y = 0
max_gidung = x[y.index(max(y))]
neobi = 0

# x의 시작좌표 ~ 가장 높은곳 까지의 면적 계산
for i in range(min(x), max_gidung+1):
    try:
        if y[x.index(i)] >= imsi_max_y:
            imsi_max_y = y[x.index(i)]
            neobi += imsi_max_y
        else:
            neobi += imsi_max_y
    except:
        neobi += imsi_max_y

# x의 끝좌표 ~ 가장 높은곳 까지의 면적 계산
imsi_max_y = 0
for i in range(max(x), max_gidung, -1):
    try:
        if y[x.index(i)] >= imsi_max_y:
            imsi_max_y = y[x.index(i)]
            neobi += imsi_max_y
        else:
            neobi += imsi_max_y
    except:
        neobi += imsi_max_y

print(neobi)
