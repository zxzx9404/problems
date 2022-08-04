a, b = map(int, input().split())
list_badak = []

for i in range(a):
    list_badak.extend(input())

count = 0

for i in range(a*b):
    if list_badak[i] == '|':
        if i >= (a-1)*b:
            continue
        elif list_badak[i+b] == '|':
            count += 1

    elif list_badak[i] == '-':
        if (i+1) % b == 0:
            continue
        elif list_badak[i+1] == '-':
            count += 1

print(a*b-count)

            




# - |
