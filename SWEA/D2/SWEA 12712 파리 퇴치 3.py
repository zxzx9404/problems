TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    delta_gase = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    delta_daegak = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    fly = 0
    for i in range(n):
        for j in range(n):
            temp = arr[i][j]
            for k in range(4):
                for u in range(1, m):
                    ni, nj = i+delta_gase[k][0]*u, j+delta_gase[k][1]*u
                    if 0 <= ni < n and 0 <= nj < n:
                        temp += arr[ni][nj]
                        
            fly = max(fly, temp)
            
            temp = arr[i][j]
            for k in range(4):
                for u in range(1, m):
                    ni, nj = i+delta_daegak[k][0]*u, j+delta_daegak[k][1]*u
                    if 0 <= ni < n and 0 <= nj < n:
                        temp += arr[ni][nj]
            fly = max(fly, temp)
    print(f'#{tc} {fly}')
            