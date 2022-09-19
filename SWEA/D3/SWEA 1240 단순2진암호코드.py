# 미리 패턴 입력
pattern = [
    '0001101', '0011001', '0010011', '0111101', '0100011',
    '0110001', '0101111', '0111011', '0110111', '0001011']


TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    # 한 줄만 봐도 되므로, 모두 0으로 이루어지지 않은 한줄만 찾아오기
    for i in arr:
        if int(i) != 0:
            arr = i
            break
    # 앞에서부터 탐색하면 오류가 남
    # 모든 패턴의 맨 마지막 숫자는 1이므로 뒤부터 탐색하기위한 시작점 찾기  
    for i in range(m-1, -1, -1):
        if arr[i] == '1':
            break

    ans = []
    # 뒤부터 패턴에 맞는 숫자를 찾음
    while i-5 > 0:
        if arr[i-6:i+1] in pattern:
            ans.append(pattern.index(arr[i-6:i+1]))
            i -= 7
        else:
            i -= 1
            
    # 뒤부터 찾았으므로 한번 뒤집어 줌
    ans = ans[::-1]
    
    dap = 0
    for i in range(8):
        if i % 2 == 0:
            dap += ans[i]*3
        else:
            dap += ans[i]

    # 조건에 따라 합을 구한 뒤 10으로 나눈 나머지 확인 후 출력
    if dap % 10 == 0:
        print(f'#{tc} {sum(ans)}')
    else:
        print(f'#{tc} 0')