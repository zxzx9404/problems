# 가지치기를 하지 않으면 시간초과 남.

def count(idx, visited, SUM):
    global minsum
    if idx >= n:
        if minsum > SUM:
            minsum = SUM
        return

    if SUM > minsum: # 가지치기
        return

    for k in range(n):
        if visited[k] == 0: # visited list를 통해 계산
            SUM += arr[idx][k]
            
            visited[k] = 1

            count(idx+1, visited, SUM)
            
            visited[k] = 0 # visited list 및 sum 원상복구
            SUM -= arr[idx][k]


TC = int(input())
for tc in range(1,TC+1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    

    visited = [0] * n
    SUM = 0
    minsum = 5000

    count(0, visited, SUM)

    print(f'#{tc} {minsum}')




# 맞지만 시간초과

def f(i, N):  # nPn 순열 만들기
    global minsum
    if i == N:
        temp = 0
        for k in range(n):
            temp += arr[k][P[k]-1]
            if temp > minsum:
                break
        else:
            minsum = min(minsum, temp)
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]



TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    arr = []
    P = []
    for x in range(1, n+1):
        arr.append(list(map(int, input().split())))
        P.append(x)
    minsum = 5000
    f(0, n)
    print(f'#{tc} {minsum}')
