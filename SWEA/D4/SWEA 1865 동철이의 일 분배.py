def dongchul(c, temp):
    global ans

    if temp <= ans:
        return

    if c == N:
        ans = max(ans, temp)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dongchul(c+1, temp * arr[c][i] / 100)
            visited[i] = 0

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0    
    visited = [0] * N

    dongchul(0, 100)

    print(f'#{tc} {ans:.6f}')