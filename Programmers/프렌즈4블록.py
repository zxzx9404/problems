def solution(m, n, board):
    answer = 0
    arr = [list(map(str, i)) for i in board]
    temp = set('1')
    
    while temp:
        # 2x2 블록 찾기
        temp = set()
        for i in range(m-1):
            for j in range(n-1):
                if arr[i][j] and arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1]:
                    temp.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
        
        # 부셔질 것들의 개수
        answer += len(temp)
        # 0으로 바꿔줌
        for i, j in temp:
            arr[i][j] = 0
        
        # 남은 블록 내려주기
        for i in range(m-2, -1, -1):
            for j in range(n):
                c = i
                while True:
                    if c < m-1 and arr[c][j] and not arr[c+1][j]:
                        arr[c][j], arr[c+1][j] = arr[c+1][j], arr[c][j]
                        c += 1
                    else:
                        break 
    return answer