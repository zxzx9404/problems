n = int(input())
list_a = []
for i in range(n):
    a, b = input().split()
    list_a.append([int(a), b])
    
list_a = sorted(list_a, key= lambda x:(x[0]))

for i in range(len(list_a)):
    print(list_a[i][0], list_a[i][1])


