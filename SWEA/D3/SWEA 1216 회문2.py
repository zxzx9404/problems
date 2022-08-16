for tc in range(10):
    num = int(input())
    arr = []
    for _ in range(100):
        arr.append(input())

    ans = 0             
    for i in range(100): 
        for k in range(100):
            temp_row = ''
            temp_col = ''
            for j in range(100-k):
                temp_row += arr[i][j+k] # 가로 계산
                temp_col += arr[j+k][i] # 세로 계산
                if temp_row == temp_row[::-1] and ans < len(temp_row):
                    ans = len(temp_row)
                if temp_col == temp_col[::-1] and ans < len(temp_col):
                    ans = len(temp_col) # 매 알파벳을 추가할때마다 회문여부 및 최장길이 여부 검사
    print(f'#{num} {ans}')