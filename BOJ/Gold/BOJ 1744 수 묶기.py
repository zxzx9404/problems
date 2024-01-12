N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
plus = []
minus = []
zero = 0
one = 0
ans = 0
for i in arr:
    if i < 0:
        minus.append(i)
    elif i == 0:
        zero += 1
    elif i == 1:
        one += 1
    elif i > 1:
        plus.append(i)

# minus
flag = False
for i in minus:
    if flag:
        ans += left*i
        flag = False
    else:
        left = i
        flag = True

# zero
if minus and flag and not zero:
    ans += left
    
# one
ans += one

# plus
plus.sort(reverse=True)
flag = False
for i in plus:
    if flag:
        ans += left*i
        flag = False
    else:
        left = i
        flag = True
        
if flag:
    ans += left

print(ans)
