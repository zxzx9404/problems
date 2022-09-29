def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

def length(a, b):
    if island[a][0] == island[b][0] or island[a][1] == island[b][1]:
        L = (abs(island[a][0] - island[b][0]) + abs(island[a][1] - island[b][1]))**2
    else:
        L = (((island[a][0] - island[b][0])**2 + (island[a][1] - island[b][1])**2)**0.5)**2
    return L

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    tax = float(input())
    rep = list(range(N))
    island = []
    for i in range(N):
        island.append([arr[i], arr2[i]])

    edge = []
    for i in range(N):
        for j in range(N):
            if i != j:
                edge.append((length(i, j)*tax, i, j))     
    edge.sort()

    ans, cnt = 0, 0
    for cost, i, j in edge:
        if find_set(i) != find_set(j):
            cnt += 1
            union(i, j)
            ans += cost
            if cnt == N-1:
                break
    print(f'#{tc} {round(ans)}')