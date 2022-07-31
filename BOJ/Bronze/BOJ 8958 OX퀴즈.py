n = int(input())

for _ in range(n):
    hap = 0
    yeonsok = 0
    for i in input():
        if i == 'O':
            yeonsok += 1
            hap += yeonsok
        else:
            yeonsok = 0
    print(hap)