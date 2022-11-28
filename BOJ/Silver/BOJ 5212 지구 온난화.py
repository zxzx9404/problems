R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
change = []
max_i, max_j, min_i, min_j = -1, -1, R, C

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            sea = 0
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= R or nj < 0 or nj >= C or arr[ni][nj] == '.':
                    sea += 1
            if sea > 2:
                change.append((i, j))
            else:
                max_i, max_j = max(i, max_i), max(j, max_j)
                min_i, min_j = min(i, min_i), min(j, min_j)
          
for i, j in change:
    arr[i][j] = '.'

for k in range(min_i, max_i+1):
    print(''.join(arr[k][min_j:max_j+1]))