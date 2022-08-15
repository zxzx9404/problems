N, K = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

count = 0
while K != 0:
    count += (K // arr[N-1])
    K %= arr[N-1]
    N -= 1

print(count)