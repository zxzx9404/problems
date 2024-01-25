import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

i, j = 0, N-1
ans = abs(arr[i] + arr[j])
ans_i, ans_j = 0, N-1

while i < j:
    temp = arr[i] + arr[j]
    
    if ans > abs(temp):
        ans = abs(temp)
        ans_i = i
        ans_j = j
        if not ans:
            break
    if temp > 0:
        j -= 1
    else:
        i += 1
    
print(arr[ans_i], arr[ans_j])
