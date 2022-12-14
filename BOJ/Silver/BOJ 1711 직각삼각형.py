import sys
input = sys.stdin.readline

N = int(input())
xx, yy = [], []
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())
    xx.append(x)
    yy.append(y)


for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            a = (xx[i] - xx[j])**2 + (yy[i] - yy[j])**2
            b = (xx[i] - xx[k])**2 + (yy[i] - yy[k])**2
            c = (xx[j] - xx[k])**2 + (yy[j] - yy[k])**2
            
            if a == b + c or b == a + c or c == a + b:
                cnt += 1

print(cnt)