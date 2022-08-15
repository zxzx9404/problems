TC = int(input())

for tc in range(1, TC+1):
    arr = []
    by33 = []    
    for _ in range(9):
        arr.append(list(map(int, input().split())))
        by33.append([])
    p = True

    ans = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(arr[i][j])
            col.append(arr[j][i])
            if i < 3:
                if j < 3:
                    by33[0].append(arr[i][j])
                elif j < 6:
                    by33[1].append(arr[i][j])
                else:
                    by33[2].append(arr[i][j])
            elif i < 6:
                if j < 3:
                    by33[3].append(arr[i][j])
                elif j < 6:
                    by33[4].append(arr[i][j])
                else:
                    by33[5].append(arr[i][j])
            else:
                if j < 3:
                    by33[6].append(arr[i][j])
                elif j < 6:
                    by33[7].append(arr[i][j])
                else:
                    by33[8].append(arr[i][j])

        for i in ans:
            if i not in row:
                p = False
        for i in ans:
            if i not in col:
                p = False
    for k in range(9):
        for m in ans:
            if m not in by33[k]:
                p = False
    if p:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')