a = int(input())
max_count = 1

for i in range(1, a+1):
    count = 1
    list_a = [a]
    b = a
    while b - i >= 0:
        list_a.append(b-i)
        count += 1
        i = list_a[count-1]
        b = list_a[count-2]
    if max_count <= count:
        max_count = count
        max_list = list_a
        
if a == 1:
    print(4)
    print('1 1 0 1')
else:
    print(max_count)
    for i in max_list:
        print(i, end=' ')