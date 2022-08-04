import sys

n = int(input())
list_a = []

for i in range(n):
    list_a.append(list(map(int, sys.stdin.readline().split())))

list_a.sort(key=lambda x: (x[0], x[1]))

for i in list_a:
    print(i[0], i[1])

# 람다의 활용 한번 더 봐두기