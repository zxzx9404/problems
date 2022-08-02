n = int(input())
switch = list(map(int, input().split()))
stu_n = int(input())

def change(n):
    if switch[n] == 0:
        switch[n] = 1
    else:
        switch[n] = 0

for _ in range(stu_n):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b-1, n, b):
            change(i)
    elif a == 2:
        change(b-1)
        for i in range((n//2)):
            if b-i-2 < 0 or b+i >= n:
                break
            elif switch[b-i-2] == switch[b+i]:
                change(b-i-2)
                change(b+i)
            else:
                break

for i in range(n):
    print(switch[i], end=' ')
    if i % 20 == 19:
        print('')
