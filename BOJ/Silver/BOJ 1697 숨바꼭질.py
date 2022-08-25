N, K = map(int, input().split())

# 같을 경우
if N == K:
    print(0)

# 동생이 더 뒤에 있을 경우
elif N > K:
    print(N-K)

#동생이 더 앞에 있는 경우
else:
    time = [0] * (K+1)

    for i in range(N, 0, -1):
        time[i-1] = N-i+1
    
    for i in range(N+1, K+1):
        time[i] = time[i-1] + 1
        if i % 2 == 0:
            time[i] = min(time[i], time[i//2]+1)
        elif i % 2 == 1:
            time[i] = min(time[i], time[i//2]+2, time[(i//2)+1]+2)
    print(time[K])