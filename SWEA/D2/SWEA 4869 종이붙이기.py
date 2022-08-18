arr = [0, 1, 3] # 초기값

for i in range(3, 31): # 문제의 최대값에 맞는 범위만큼의 정답 리스트를 미리 만들어 둠
    arr.append(arr[i-2]*2 + arr[i-1])

TC = int(input())

for tc in range(1, TC+1): # 해당하는 값 입력받아 출력
    a = int(input())
    print(f'#{tc} {arr[a//10]}')