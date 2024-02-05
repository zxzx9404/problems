from sys import stdin, maxsize
input = stdin.readline

N = int(input())
M = int(input())
bus = [[maxsize]*N for _ in range(N)]
route = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if bus[a-1][b-1] > c:
        bus[a-1][b-1] = c
        route[a-1][b-1] = [a, b]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if bus[i][j] > bus[i][k] + bus[k][j]:
                bus[i][j] = bus[i][k] + bus[k][j]
                route[i][j] = route[i][k][:len(route[i][k])-1] + route[k][j]

for i in range(N):
    for j in range(N):
        if bus[i][j] == maxsize:
            bus[i][j] = 0
        print(bus[i][j], end=' ')
    print()

for i in range(N):
    for j in range(N):
        if not bus[i][j]:
            print(0)
        else:
            print(len(route[i][j]), *route[i][j])
