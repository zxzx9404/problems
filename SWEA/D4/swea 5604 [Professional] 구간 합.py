tc = int(input())

def jarihap(x):
    hap = 0
    if x == '-1':
        return 0
    for i in range(len(x)):
        if len(x) == 1: #한자리 수
            for m in range(int(x)):
                hap += m+1
        else:
            if int(x[i]) == 0:
                for j in range(1):
                    if i == len(x) - 1: #마지막 자리 수
                        if j == 0:
                            hap += int(x[0:len(x)-1])*45
                    else: # 기타 자리 수
                        if j == 0 :
                            hap += int(x[0:i])*45*(10**(len(x)-i-1))
                            hap += int(x[i])*(int(x[i+1:])+1)
            else:
                for j in range(int(x[i])):
                    if i == len(x) - 1: #마지막 자리 수
                        if j == 0:
                            hap += int(x[0:len(x)-1])*45
                            hap += j+1
                        else:
                            hap += j+1
                    elif i == 0: #첫번째 자리 수
                        if j == 0:
                            hap += int(x[0])*(int(x[1:])+1)
                        else:
                            hap += j * (10**(len(x)-1))
                    else: # 기타 자리 수
                        if j == 0 :
                            hap += int(x[0:i])*45*(10**(len(x)-i-1))
                            hap += int(x[i])*(int(x[i+1:])+1)
                        else:
                            hap += j * (10**(len(x)-i-1))
    return hap

for i in range(tc):
    a, b = input().split()
    c = jarihap(b)
    d = jarihap(str(int(a)-1))
    print(f'#{i+1} {c-d}')
