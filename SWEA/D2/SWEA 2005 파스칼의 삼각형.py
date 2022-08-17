TC = int(input())

for tc in range(1, TC+1):
    arr = []
    n = int(input())
    for i in range(1, n+1):
        arr.append([1]*i)                                 # 먼저 모양에 맞는 크기의 2차원 arr를
    if n > 2:                                             # 모두 1의 값으로 만듬
        for j in range(2, n):                             # n > 2일때만 값의 변경이 필요
            for k in range(1, j):
                arr[j][k] = arr[j-1][k-1] + arr[j-1][k]   # 조건식에 따른 값 변경
    print(f'#{tc}')
    for i in arr:                                         # 출력 과정
        for j in i:
            print(j, end=' ')
        print('')
    
    
