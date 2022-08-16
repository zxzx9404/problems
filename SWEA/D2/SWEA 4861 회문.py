TC = int(input())

for tc in range(1, TC+1):
    arr = []
    N, M = map(int, input().split())
    for _ in range(N):
        arr.append(input())               # 문자열은 순회가능하므로 그대로 인풋

    p = False                             # 정답 찾을 시 반복문 탈출을 위한 변수
    for m in range(N):
        if p:
            break
        for i in range(N-M+1):            # 한 줄의 길이 - 찾아야할 문자열의 길이 + 1
            if p:
                break
            temp_row = ''                 # 한번의 for문을 돌며 열과 행을 동시 계산
            temp_col = ''
            for j in range(M):
                temp_row += arr[m][j+i]
                temp_col += arr[j+i][m]
            if temp_row == temp_row[::-1]:# 행에서 맞으면 정답을 저장
                p = True
                ans = temp_row
            elif temp_col == temp_col[::-1]: # 열에서 맞으면 정답을 저장
                p = True
                ans = temp_col
    print(f'#{tc} {ans}')
