case_num = int(input())

for i in range(case_num):
    case = input()
    y = int(case[:4])
    m = int(case[4:6])
    d = int(case[6:])

    if m == 4 or m == 6 or m == 9 or m == 11:
        if 0<d<31:
            print(f'#{i+1} {case[:4]}/{case[4:6]}/{case[6:]}')
        else:
            print(f'#{i+1} -1')
    elif m == 2:
        if 0<d<29:
            print(f'#{i+1} {case[:4]}/{case[4:6]}/{case[6:]}')
        else:
            print(f'#{i+1} -1')
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 0<d<32:
            print(f'#{i+1} {case[:4]}/{case[4:6]}/{case[6:]}')
        else:
            print(f'#{i+1} -1')
    else:
        print(f'#{i+1} -1')


