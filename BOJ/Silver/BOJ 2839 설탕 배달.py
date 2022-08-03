k = int(input())

if (k % 5) % 3 == 0:
    print(k//5+(k % 5)//3)
else:
    count = 1
    while True:
        k = k-3
        if k < 0:
            print('-1')
            break
        if k % 5 == 0:
            print(k//5+count)
            break
        else:
            count += 1