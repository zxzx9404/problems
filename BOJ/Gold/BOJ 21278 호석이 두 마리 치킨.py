from collections import defaultdict

N, M = map(int, input().split())
adjList = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adjList[a-1].append(b-1)
    adjList[b-1].append(a-1)
    

time = defaultdict(dict)

for i in range(N):
    time[i][i] = 0
    q = [i]
    while q:
        k = q.pop(0)
        for nearPoint in adjList[k]:
            if i != nearPoint and time[i].get(nearPoint) == None:
                time[i][nearPoint] = time[i][k] + 1
                q.append(nearPoint)

ans = 10**15
for i in range(N):
    for j in range(N):
        if i != j:
            temp = 0
            for k in range(N):
                temp += min(time[k][i], time[k][j])
            if ans > temp:
                ans = temp
                dap = [i+1, j+1, ans*2]

print(*dap)
