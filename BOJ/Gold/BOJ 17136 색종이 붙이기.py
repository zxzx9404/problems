# 1048ms
def dfs(recur, cnt):
    global ans
    
    if ans <= cnt:
        return
    
    if recur == 100:  # 끝에 도달하면 판단
        ans = min(ans, cnt)
        return

       
    i = recur // 10  # recursion 횟수에 따라 i열번호 j열번호 부여 
    j = recur % 10
    
    
    if arr[i][j]:  # 1이라면
        for n in range(5):  # 각 사이즈의 색종이를 비교하며 덮을수 있다면 덮고 재귀식 진행
            ni, nj = i + n, j + n
            if ni < 10 and nj < 10 and arr[ni][nj] and paper[n]:
                for m in range(n+1):
                    if arr[i+m][j:j+n+1] != ones[n]:
                        break
                else:
                    for m in range(n+1):
                        arr[i+m][j:j+n+1] = zeros[n]
                    paper[n] -= 1
                    dfs(recur+n+1, cnt+1)
                    paper[n] += 1
                    for m in range(n+1):
                        arr[i+m][j:j+n+1] = ones[n]
                        
    else:  # 0이면 그냥 바로 다음거
        dfs(recur+1, cnt)
                    

arr = [list(map(int, input().split())) for _ in range(10)]

ans = 26  # 종이의 최대 장수 + 1
paper = [5, 5, 5, 5, 5]  # 남은 종이의 수

# 각 종이별로 덮을때, 복구해줄때의 형태를 세팅
ones = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
zeros = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]

dfs(0, 0)

print(ans) if ans != 26 else print(-1)
