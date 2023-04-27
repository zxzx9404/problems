def find(x):
    if rep[x] != x:
        return find(rep[x])
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        rep[x] = y
    else:
        rep[y] = x


N = int(input())
rep = [i for i in range(N)]

for _ in range(N-2):
    a, b = map(int, input().split())
    a -= 1; b -=1
    union(a, b)

for i in range(N):
    for j in range(N):
        if find(i) != find(j):
            print(i, j)
            quit()