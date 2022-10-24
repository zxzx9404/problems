# PyPy3 : 2044ms

def bfs(cnt):
    if cnt == 81:
        for k in arr:
            print(*k)
        quit()
    
    i = cnt // 9
    j = cnt % 9

    if not arr[i][j]:
        temp = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        temp2 = set()
        for k in range(9):
                temp2.add(arr[k][j])
                temp2.add(arr[i][k])
        
        ni, nj = (i//3)*3, (j//3)*3
        
        for m in range(3):
            for n in range(3):
                temp2.add(arr[ni+m][nj+n])
             
        temp = list(temp-temp2)

        for k in temp:
            arr[i][j] = k
            bfs(cnt+1)
            arr[i][j] = 0
    
    else:
        bfs(cnt+1)
    

arr = [list(map(int, input().split())) for _ in range(9)]

bfs(0)