N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(6):
    gap = arr[0][i]
    temp = 0
    for j in range(N):
        idx = arr[j].index(gap)
        
        if idx == 0 or idx == 5:
            temp += max(arr[j][1], arr[j][2], arr[j][3], arr[j][4])
            gap = arr[j][5-idx]
        elif idx == 1 or idx == 3:
            temp += max(arr[j][0], arr[j][2], arr[j][5], arr[j][4])
            gap = arr[j][4-idx]
        elif idx == 2 or idx == 4:
            temp += max(arr[j][0], arr[j][1], arr[j][5], arr[j][3])
            gap = arr[j][6-idx]
            
    ans = max(ans, temp)

print(ans)