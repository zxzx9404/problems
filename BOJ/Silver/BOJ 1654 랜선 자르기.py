n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))


left, right = 1, max(arr)
while left <= right:
    lan = 0
    mid = (left + right)//2
    for i in arr:
        lan += i//mid
    if lan >= k:
        left = mid + 1
    else:
        right = mid - 1
print(right)

# 해당 이분탐색은 가능한 길이 중 최대를 구해야 하기 때문에
# right를 출력해야 함


