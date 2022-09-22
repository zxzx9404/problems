a, b = map(int, input().split())

cnt = 0
p = True
while b>a:
    temp = b
    if str(b)[-1] == '1':
        b = int(str(b)[:len(str(b))-1])
    elif b % 2 == 0:
        b //= 2
    cnt += 1
    if a == b:
        break
    
    elif b < a or temp == b:
        p = False
        break

if p:
    print(cnt+1)
else:
    print(-1)