def wall(a):
    if a == 1:
        return 2
    elif a == 2:
        return 1
    elif a == 3:
        return 4
    return 3

delta = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]

TC = int(input())

for tc in range(1, TC+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]   

    for m in range(M):
        arr2 = [[0]*N for _ in range(N)]
        fight = []
        for i in range(K):
            if arr[i] != []:
                arr[i][0] += delta[arr[i][3]][0]
                arr[i][1] += delta[arr[i][3]][1]

                if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                    arr[i][2] //= 2
                    arr[i][3] = wall(arr[i][3])


                arr2[arr[i][0]][arr[i][1]] += 1

                if arr2[arr[i][0]][arr[i][1]] > 1 and [arr[i][0], arr[i][1]] not in fight:
                    fight.append([arr[i][0], arr[i][1]])

                if arr[i][2] == 0:
                    arr[i] = []
        while fight:
            y, x = fight.pop(0)
            idx_list = []
            maxG, sumG = 0, 0
            for i in range(K):
                if arr[i] != []:
                    if arr[i][0] == y and arr[i][1] == x:
                        idx_list.append(i)
                        sumG += arr[i][2]
                        if maxG < arr[i][2]:
                            maxG = arr[i][2]
                            max_idx = i
            for j in idx_list:
                if max_idx == j:
                    arr[max_idx][2] = sumG
                else:
                    arr[j] = []
            
    hap = 0
    for jj in range(K):
        if arr[jj] != []:
            hap += arr[jj][2]
    print(f'#{tc} {hap}')