import sys

input = sys.stdin.readline

n = int(input())
arr = [0]*8001
sum = 0
max_n = -4000
min_n = 4000
for _ in range(n):
    a = int(input())
    if a != 0:
        arr[a+4000] += 1
    else:
        arr[4000] += 1
    sum += a
    if max_n <= a:
        max_n = a
    if min_n >= a:
        min_n = a


# arr[4000] = 0의 개수
# arr[0~3999] = -4000~-1의 개수
# arr[4001~8000] = 1~4000의 개수    

# 산술 평균
print(round(sum/n))

# 중앙값
idx = -1
jung = 0
while jung < (n//2)+1:
    idx += 1
    jung += arr[idx]

print(idx-4000)
# 최빈값

max_arr = []
idx_list = []
for i in range(8001):
    if arr[i] == max(arr):
        max_arr.append(arr[i])
        idx_list.append(i)
        
if len(max_arr) == 1:
    print(idx_list[0]-4000)
else:
    print(idx_list[1]-4000)



# 범위
print(max_n-min_n)