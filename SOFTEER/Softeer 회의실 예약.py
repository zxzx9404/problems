N, M = map(int, input().split())

dct = dict()
for _ in range(N):
    dct[input()] = [[9, True], [10, True], [11, True], [12, True], [13, True], [14, True], [15, True], [16, True], [17, True], [18, False]]

for _ in range(M):
    room, start, end = input().split()
    start, end = int(start)-9, int(end)-9

    for i in range(start, end):
        dct[room][i][1] = False
    
arr = sorted(dct.items())
cnt = 0

for room, resv in arr:
    cnt += 1
    temp = []
    start_time, end_time = 0, 0
    for time in resv:
        if time[1] and not start_time:
            start_time = time[0]
        elif not time[1] and start_time:
            end_time = time[0]
            if start_time == 9:
                start_time = '09'
            temp.append(f'{start_time}-{end_time}')
            start_time = 0

    print(f'Room {room}:')
    if not temp:
        print('Not available')
    else:
        print(f'{len(temp)} available:')
        for k in temp:
            print(k)
    if cnt < N:
        print('-----')