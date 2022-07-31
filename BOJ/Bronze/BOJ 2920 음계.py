umgye = list(map(int, input().split()))
a = 0
for i in range(len(umgye)):
    if umgye[i] == i+1:
        a += 1
    elif umgye[i] == 8-i:
        a -= 1
    
if a == 8:
    print('ascending')
elif a == -8:
    print('descending')
else:
    print('mixed')