import sys
sys.setrecursionlimit(10000000)

def danzi(i, j):
    temp_i = i
    while 0 <= temp_i+1 < n and arr[temp_i+1][j] != '0' and arr[temp_i+1][j] != str(cnt+1):
        temp_i += 1
        arr[temp_i][j] = str(cnt+1)
        danzi(temp_i, j)
    temp_i = i
    while 0 <= temp_i-1 < n and arr[temp_i-1][j] != '0' and arr[temp_i-1][j] != str(cnt+1):
        temp_i -= 1
        arr[temp_i][j] = str(cnt+1)
        danzi(temp_i, j)
    temp_j = j
    while 0 <= temp_j+1 < n and arr[i][temp_j+1] != '0' and arr[i][temp_j+1] != str(cnt+1):
        temp_j += 1
        arr[i][temp_j] = str(cnt+1)
        danzi(i, temp_j)
    temp_j = j
    while 0 <= temp_j-1 < n and arr[i][temp_j-1] != '0' and arr[i][temp_j-1] != str(cnt+1):
        temp_j -= 1
        arr[i][temp_j] = str(cnt+1)
        danzi(i, temp_j)




n = int(input())

arr = []

for _ in range(n):
    a = input()
    temp = []
    for tt in a:
        temp.append(tt)
    arr.append(temp)

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            cnt += 1
            arr[i][j] = str(cnt+1)
            danzi(i, j)


ans = []
for k in range(2, cnt+2):
    temp = 0
    for m in range(n):
        for u in range(n):
            if arr[m][u] == str(k):
                temp += 1
    ans.append(temp)
    
ans.sort()

print(cnt)
for an in ans:
    print(an)