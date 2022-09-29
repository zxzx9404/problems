def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)


TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    rep = list(range(N+1))
    for _ in range(M):
        a, b = map(int, input().split())
        if find_set(a) != find_set(b):
            union(a, b)
    cnt = 0
    for i in range(1, N+1):
        if find_set(i) == i:
            cnt +=1
    print(f'#{tc} {cnt}')