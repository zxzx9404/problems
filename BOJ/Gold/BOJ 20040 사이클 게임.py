import sys
input = sys.stdin.readline

def find(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        rep[x] = y
    else:
        rep[y] = x

N, M = map(int, input().split())
rep = [i for i in range(N)]

for turn in range(M):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(turn+1)
        break
    union(a, b)
else:
    print(0)