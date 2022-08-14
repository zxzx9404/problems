a, b = map(int, input().split())

for i in range(a, b+1):
    p = True
    if i == 1:
        p = False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            p = False
            break
    if p:
        print(i)