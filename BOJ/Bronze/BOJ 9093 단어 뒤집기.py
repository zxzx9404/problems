import sys

n = int(input())

for i in range(n):
    list_a = list(map(str, sys.stdin.readline().split()))
    for j in range(len(list_a)):
        print(list_a[j][::-1], end=' ')
    print('')