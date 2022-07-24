case_num = int(input())

for i in range(case_num):
    temp_list = map(int, input().split())
    add = 0
    for j in temp_list:
        if j % 2 == 1:
            add += j
    print(f'#{i+1} {add}')