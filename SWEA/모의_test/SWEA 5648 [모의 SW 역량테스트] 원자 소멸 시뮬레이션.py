TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        # 절대값을 쓰지 않고 편하게 계산하기 위해 음수를 없애줌
        arr[i][0] += 1000
        arr[i][1] += 1000
    # 잠재적으로(선충돌로 인한 방해를 제외하고) 충돌이 가능한 모든 경우의 수를 담는 list
    possible = []
    # 충돌되어 사라진 원자인지를 판단하는 list
    left = [1] * N
    # 3개 이상의 원자가 같이 충돌할 경우, 충돌 시간을 통해 같은 충돌인지를 파악하기 위한 list
    out_time = [0] * N
    ans = 0
    
    # 모든 원자를 순회하면서
    for i in range(N):
        # 위로 이동하는 원자일 경우
        if arr[i][2] == 0:
            for j in range(N):
                # 자신보다 좌상단에 위치하며 우측으로 오고있는 원자 and 거리상 충돌이 가능
                if arr[j][1] > arr[i][1] and arr[j][1] - arr[i][1] == arr[i][0] - arr[j][0] and arr[j][2] == 3:
                    possible.append([arr[j][1] - arr[i][1], i, j])
                # 자신보다 우상단에 위치하며 좌측으로 오고있는 원자 and 거리상 충돌이 가능
                elif arr[j][1] > arr[i][1] and arr[j][1] - arr[i][1] == arr[j][0] - arr[i][0] and arr[j][2] == 2:
                    possible.append([arr[j][1] - arr[i][1], i, j])
                # 자신과 x축 값이 같으면서 아래로 오고있는 원자(무조건 충돌 가능)
                elif arr[j][1] > arr[i][1] and arr[j][0] == arr[i][0] and arr[j][2] == 1:
                    possible.append([(arr[j][1] - arr[i][1])/2, i, j])
        elif arr[i][2] == 1:
            for j in range(N):
                if arr[j][1] < arr[i][1] and arr[i][1] - arr[j][1] == arr[i][0] - arr[j][0] and arr[j][2] == 3:
                    possible.append([arr[i][1] - arr[j][1], i, j])
                elif arr[j][1] < arr[i][1] and arr[i][1] - arr[j][1] == arr[j][0] - arr[i][0] and arr[j][2] == 2:
                    possible.append([arr[i][1] - arr[j][1], i, j])
                elif arr[i][1] > arr[j][1] and arr[j][0] == arr[i][0] and arr[j][2] == 0:
                    possible.append([(arr[i][1] - arr[j][1])/2, i, j])
        elif arr[i][2] == 2:
            for j in range(N):
                if arr[i][0] > arr[j][0] and arr[i][0] - arr[j][0] == arr[j][1] - arr[i][1] and arr[j][2] == 1:
                    possible.append([arr[i][0] - arr[j][0], i, j])
                elif arr[i][0] > arr[j][0] and arr[i][0] - arr[j][0] == arr[i][1] - arr[j][1] and arr[j][2] == 0:
                    possible.append([arr[i][0] - arr[j][0], i, j])
                elif arr[i][0] > arr[j][0] and arr[j][1] == arr[i][1] and arr[j][2] == 3:
                    possible.append([(arr[i][0] - arr[j][0])/2, i, j])
        elif arr[i][2] == 3:
            for j in range(N):
                if arr[i][0] < arr[j][0] and arr[j][0] - arr[i][0] == arr[j][1] - arr[i][1] and arr[j][2] == 1:
                    possible.append([arr[j][0] - arr[i][0], i, j])
                elif arr[i][0] < arr[j][0] and arr[j][0] - arr[i][0] == arr[i][1] - arr[j][1] and arr[j][2] == 0:
                    possible.append([arr[j][0] - arr[i][0], i, j])
                elif arr[i][0] < arr[j][0] and arr[j][1] == arr[i][1] and arr[j][2] == 2:
                    possible.append([(arr[j][0] - arr[i][0])/2, i, j])
    
    # 첫 번째 인자(충돌시간)를 기준으로 정렬
    possible.sort()

    # 가능한 모든 충돌을 검사
    for time, i, j in possible:
        # 아직 두 원자 모두 남아있다면 충돌처리
        if left[i] and left[j]:
            ans += (arr[i][3] + arr[j][3])
            left[i], left[j] = 0, 0
            out_time[i] = time
            out_time[j] = time
        # 두 원자중 남아있다면, 없는 원자가 충돌된 시간과 같을 시 다자충돌로 판단하여 제거
        elif left[i] and not left[j]:
            if time == out_time[j]:
                ans += arr[i][3]
                left[i] = 0
        elif not left[i] and left[j]:
            if time == out_time[i]:
                ans += arr[j][3]
                left[j] = 0
                
    print(f'#{tc} {ans}')