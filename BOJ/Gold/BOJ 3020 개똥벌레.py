import sys
input = sys.stdin.readline

N, H = map(int, input().split())
bottom, top = [], []
half_len = N//2
for i in range(half_len):
    bot_obstacle = int(input())
    top_obstacle = int(input())
    
    bottom.append(bot_obstacle)
    top.append(top_obstacle)

bottom.sort()
top.sort()

def binary(cave, height):
    left, right = 0, half_len - 1
    while left <= right:
        mid = (left + right) // 2
        if cave[mid] <= height:
            left = mid + 1
        else:
            right = mid - 1
    return half_len - (right + 1)

ans = N
cnt = 0

for i in range(1, H+1):
    temp = binary(bottom, i-1) + binary(top, H-i)

    if ans > temp:
        ans = temp
        cnt = 1
    elif ans == temp:
        cnt += 1

print(ans, cnt)