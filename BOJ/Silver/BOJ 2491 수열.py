num = int(input())
arr = list(map(int, input().split()))

max_c = 0
count = 0

for i in range(num-1):
    if arr[i] <= arr[i+1]:
        count += 1
    else:
        count = 0
        
    if max_c < count:
        max_c = count

count = 0

for i in range(num-1):
    if arr[i] >= arr[i+1]:
        count += 1
    else:
        count = 0
        
    if max_c < count:
        max_c = count            

print(max_c+1)