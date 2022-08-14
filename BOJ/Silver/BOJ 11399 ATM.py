N = int(input())

arr = list(map(int, input().split()))

arr.sort()
ans = 0
j = 0
for i in range(N, 0, -1):
    ans += arr[j] * i
    j += 1
print(ans)