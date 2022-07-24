case_num = int(input())

for i in range(case_num):
    a = b = 0
    a, b = map(int, input().split())
    if a > b:
        print(f'#{case_num+1} >')
    elif a < b:
        print(f'#{case_num+1} <')
    elif a == b:
        print(f'#{case_num+1} =')
