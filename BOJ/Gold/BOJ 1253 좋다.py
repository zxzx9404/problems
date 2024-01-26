from collections import defaultdict

def binary_search(num, idx):
    left, right = 0, N-1
    
    while left < right:
        m = arr[left] + arr[right]
        
        if m == num:
            if left == idx:
                left += 1
            elif right == idx:
                right -= 1
            else:
                return True
        
        elif m < num:
            left += 1
        else:
            right -= 1
    
    return False

N = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
goods = defaultdict(int)

for i in range(N):
    if goods[i]:
        if goods[i] == 1: ans += 1
        continue
    
    t = binary_search(arr[i], i)
    if t:
        ans += 1
        goods[i] = 1
    else:
        goods[i] = 2

print(ans)
