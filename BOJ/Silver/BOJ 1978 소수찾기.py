n = int(input())

list_a = list(map(int, input().split()))
count = 0
for i in list_a:
    imsi_count = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j != 0:
            imsi_count += 1
    if imsi_count == i-2:
        count += 1         
            

print(count)
