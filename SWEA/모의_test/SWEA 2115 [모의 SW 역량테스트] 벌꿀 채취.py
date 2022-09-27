import sys
sys.stdin = open('input.txt', 'r')

def f(c, temp, lst):
    global temp1
    temp1 = max(temp1, temp)

    for ii in range(M):
        if not visited[ii] and c + lst[ii] <= C:
            visited[ii] = 1
            f(c + lst[ii], temp + lst[ii]*lst[ii], lst)
            visited[ii] = 0

def ff(c, temp, lst):
    global temp2
    temp2 = max(temp2, temp)

    for ii in range(M):
        if not visited[ii] and c + lst[ii] <= C:
            visited[ii] = 1
            ff(c + lst[ii], temp + lst[ii]*lst[ii], lst)
            visited[ii] = 0

TC = int(input())

for tc in range(1, TC+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    visited = [0] * C

    for i in range(N):
        for j in range(N-M+1):
            temp1 = 0
            lst1 = arr[i][j:j+M]
            f(0, 0, lst1)
            if j+2*M <= N:
                for jj in range(j+M, N-M+1):
                    temp2 = 0
                    lst2 = arr[i][jj:jj+M]
                    ff(0, 0, lst2)
                    ans = max(temp1 + temp2, ans)
            for k in range(i+1, N):
                for m in range(N-M+1):
                    temp2 = 0
                    lst2 = arr[k][m:m+M]
                    ff(0, 0, lst2)
                    ans = max(temp1 + temp2, ans)

    print(f'#{tc} {ans}')