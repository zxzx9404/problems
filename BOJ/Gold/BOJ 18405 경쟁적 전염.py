from collections import defaultdict

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
X, Y = X-1, Y-1
temp = defaultdict(list)
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]


for i in range(N):
    for j in range(N):
        if arr[i][j]:
            temp[arr[i][j]].append((i, j))

while S and temp:
    S -= 1
    temp = sorted(temp.items())
    next = defaultdict(list)
    for i, j in temp:
        for x, y in j:
            for di, dj in delta:
                ni, nj = x + di, y + dj
                if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
                    arr[ni][nj] = i
                    next[i].append((ni, nj))
                    if ni == X and nj == Y:
                        print(i)
                        quit()
    temp = next

print(arr[X][Y])