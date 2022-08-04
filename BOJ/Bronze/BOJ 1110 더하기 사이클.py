a = int(input())
num = a
count = 0

while True:
    x = num // 10
    y = num % 10
    z = (x+y) % 10
    num = (y * 10) + z
    count += 1
    if a == num:
        print(count)
        break