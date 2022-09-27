def produce(c, temp):
    global ans

    if c == N:
        ans = min(ans, temp)
        return
    
    if temp >= ans:
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            produce(c+1, temp + arr[c][i])
            visited[i] = 0

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**10        
    visited = [0] * N

    produce(0, 0)

    print(f'#{tc} {ans}')