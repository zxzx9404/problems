def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

TC = int(input())

for tc in range(1, TC+1):
    V, E = map(int, input().split())
    
    edge = []

    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append((u, v, w))
    
    edge.sort(key=lambda x : x[2])

    rep = list(range(V+1))
    
    cnt, total = 0, 0

    for u, v, w in edge:
        if find_set(u) != find_set(v):
            cnt += 1
            union(u, v)
            total += w
            if cnt == V:
                break
            
    print(f'#{tc} {total}')