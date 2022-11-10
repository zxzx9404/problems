H, W = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, W-1):
    low_max = min(max(arr[:i]), max(arr[i+1:]))

    if arr[i] < low_max:
        ans += low_max - arr[i]

print(ans)