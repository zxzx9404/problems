case_num = int(input())

for i in range(case_num):
    temp_list = []
    temp_list = list(map(int, input().split()))
    max_num = 0
    for j in range(len(temp_list)):
        if j == 0 or temp_list[j] > max_num:
            max_num = temp_list[j]
    print(f'#{i+1} {max_num}')
