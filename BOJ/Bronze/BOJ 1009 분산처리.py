tc_num = int(input())

for i in range(tc_num):
    a = b = 0
    a, b = map(int, input().split())
    data = a**b
    print(data % 10)
