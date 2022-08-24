for _ in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))
    i = 1
    while True:
        if arr[0] - i <= 0: # 값이 0 이하가 되는 경우
            arr.pop(0)      # 첫 값 삭제
            arr.append(0)   # 0 추가
            break
        else:
            temp = arr.pop(0) # 첫 값 pop
            temp -= i         # 지정된 값 빼줌
            arr.append(temp)  # 끝에 더해줌
        i += 1
        if i == 6:            # 5까지가 한 사이클이므로 다시 초기화
            i = 1
    print(f'#{tc}', end=' ')
    print(*arr)