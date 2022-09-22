N, M = map(int, input().split())

name = {}

for _ in range(N):
    name[input()] = 1

cnt = 0
for _ in range(M):
    if name.get(input()) == 1:
        cnt += 1
print(cnt)