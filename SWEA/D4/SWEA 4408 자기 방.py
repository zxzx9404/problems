def max(list):  # max 함수 구현
    max = 0
    for i in range(len(list)):
        if max <= list[i]:
            max = list[i]
    return max
            
TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    arr = []
    hall = [0]*200        # 200칸의 복도 생성
    for _ in range(n):
        a, b = map(int, input().split())
        if a % 2 == 0:
            a -= 1
        if b % 2 == 0:
            b -= 1
        arr.append([a//2, b//2]) # 방 번호가 아닌, 지나야 할 복도를 기록
        
    for i in range(n):
        if arr[i][0] < arr[i][1]: # 출발 번호가 도착 번호보다 큰 경우
            for j in range(arr[i][0], arr[i][1]+1):
                hall[j] += 1
        else: # 반대의 경우
            for j in range(arr[i][1], arr[i][0]+1):
                hall[j] += 1
    count = max(hall)

    print(f'#{tc} {count}')