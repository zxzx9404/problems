n = int(input())
list_a = []

for i in range(n):
    a = input()
    list_a.append(a)

list_a = list(set(list_a))
list_a.sort()
list_a.sort(key=len) #sort는 문자열도 가능하고, key값을 부여해서 len또한 가능

for i in list_a:
    print(i)