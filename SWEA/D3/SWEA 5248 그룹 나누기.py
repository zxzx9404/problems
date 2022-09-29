def find_set(x):
    while x != stu[x]:
        x = stu[x]
    return x

def union(x, y):
    stu[find_set(y)] = find_set(x)

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    stu = list(range(N+1))
    
    for i in range(M):
        a, b = arr[i*2], arr[i*2+1]
        union(a, b)

    cnt = 0
    for j in range(1, N+1):
        if stu[j] == j:
            cnt += 1

    print(f'#{tc} {cnt}')