n = int(input())

for i in range(n):
    ps = input()
    ps_list = []
    for k in ps:
        ps_list.append(k) 
    count = 0
    if len(ps_list) % 2 == 1:
        print('NO')
    else:   
        while True:
            if ps_list[count] == '(' and ps_list[count+1] == ')':
                del ps_list[count]
                del ps_list[count]
                count = -1
                if ps_list == []:
                    print('YES')
                    break
            if count+1 == len(ps_list)-1:
                print('NO')
                break
            count += 1

'''
쉬운 문제라고 생각했는데 생각보다 오류가 너무 많이 났다.
코드를 짤 때 조금 더 경우의 수를 생각해보자.
'''