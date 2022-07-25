case_num = int(input())

for i in range(case_num):
    temp_list = []
    avg = 0
    temp_list = list(map(int, input().split()))
    avg = int(round(sum(temp_list) / len(temp_list), 0))
    print(f'#{i+1} {avg}')