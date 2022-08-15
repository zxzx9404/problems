def max(list):
    max = 0
    for i in list:
        if len(i) > max:
            max = len(i)
    return max

TC = int(input())

for tc in range(1,TC+1):
    arr = []
    for i in range(5):
        arr.append(input())
    for i in range(5):
        if len(arr[i]) < max(arr):
            arr[i] += '+'*(max(arr)-len(arr[i])) # 자릿수가 다를경우 부족한 부분에 '+'를 삽입
    
    print(f'#{tc}', end=' ')    
    for j in range(max(arr)):
        for i in range(5):
            if arr[i][j] != '+': # 출력할 땐 '+'를 빼줌
                print(arr[i][j], end='')
    print('')
