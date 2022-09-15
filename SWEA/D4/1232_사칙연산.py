for tc in range(1, 11):
    n = int(input())
    arr = [0]
    for _ in range(n):
        a = input().split()
        # 연산자일 경우 연산자와 자식 노드 번호 정보를 저장
        if len(a) == 4:
            arr.append(a[1:])
        else:
            # 숫자일 경우 숫자만 저장
            arr.append(int(a[1]))
            
    for i in range(n, 0, -1):
        # 리스트 형태(==연산자)이면, 필요한 연산 수행 후 결과를 입력
        if type(arr[i]) == list:
            if arr[i][0] == '+':
                arr[i] = arr[int(arr[i][1])] + arr[int(arr[i][2])]
            elif arr[i][0] == '-':
                arr[i] = arr[int(arr[i][1])] - arr[int(arr[i][2])]
            elif arr[i][0] == '*':
                arr[i] = arr[int(arr[i][1])] * arr[int(arr[i][2])]
            elif arr[i][0] == '/':
                arr[i] = arr[int(arr[i][1])] / arr[int(arr[i][2])]
                
    print(f'#{tc} {int(arr[1])}')
