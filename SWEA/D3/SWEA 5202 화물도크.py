TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 끝나는 시간 // 같다면 시작하는 시간을 기준으로 sort
    arr = sorted(arr, key= lambda x : (x[1], x[0]))

    cnt = 1
    # 제일 먼저 끝나는 작업이 끝나는 시간
    end_time = arr[0][1]

    # 첫 작업이 끝난 이후, 남은 작업 중 제일 먼저 끝나는 작업을 택함
    for i in range(1, n):
        if arr[i][0] >= end_time:
            cnt += 1
            end_time = arr[i][1]

    print(f'#{tc} {cnt}')