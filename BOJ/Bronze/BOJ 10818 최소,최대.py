n = int(input())
list_n = list(map(int, input().split()))
kun = list_n[0]
jagun = list_n[0]

for i in list_n:
    if i > kun:
        kun = i
    elif i < jagun:
        jagun = i

print(jagun, kun)