def f(cnt, lst):
    if cnt == 3:
        baseball.append(lst)
        return
    
    for i in range(3):
        if not visited[i]:
            visited[i] = 1
            f(cnt+1, lst + [temp[i]])
            visited[i] = 0

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
baseball = []
visited = [0]*3

for i in range(1<<9):
    temp = []
    for j in range(9):
        if i & (1<<j):
            temp.append(j+1)
            if len(temp) > 3:
                break
    if len(temp) == 3:
        f(0, [])
        
for nums, stk, ball in arr:
    nums = str(nums)
    k = 0
    while k < len(baseball):
        stk_k, ball_k = 0, 0
        for o in range(3):
            if int(nums[o]) == baseball[k][o]:
                stk_k += 1
            elif int(nums[o]) in baseball[k]:
                ball_k += 1
        if stk_k != stk or ball_k != ball:
            baseball.pop(k)
        else:
            k += 1

print(len(baseball))