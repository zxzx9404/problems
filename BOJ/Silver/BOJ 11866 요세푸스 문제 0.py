a, b =map(int, input().split())
i = b-1

list_a = [i for i in range(1, a+1)]
list_b = []
count = 0

print('<', end='')
while True:
    if list_a == []:
        break
    if i >= len(list_a):
        i = i % len(list_a)
    if list_a[i] not in list_b:
        count += 1
        if count != a:
            print(list_a[i], end=', ')
            list_b.append(list_a.pop(i))
            i += b-1
            continue
        elif count == a:
            print(list_a[i], end='')
            list_b.append(list_a.pop(i))
            i += b-1
            continue
    i += b
print('>')