N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
rep = [ i for i in range(N*M)]


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


direction = {'D' : (1, 0), 'U' : (-1, 0), 'L' : (0, -1), 'R' : (0, 1)}
ans = N*M

for i in range(N):
    for j in range(M):
        di, dj = direction[arr[i][j]]
        ni, nj = i + di, j + dj
        union(i*M + j, ni*M + nj)


ans = 0

for i in range(N*M):
    if i == find(i):
        ans += 1

print(ans)
