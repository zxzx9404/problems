def binary(o):
    temp = ''
    for i in o:
        if i.isdigit():
            temp2 = str(bin(int(i)))[2:]
        else:
            temp2 = str(bin(ord(i)-55))[2:]
        if len(temp2) != 4:
            temp2 = '0'*(4-len(temp2)) + temp2
        temp += temp2
    temp = '0'*12 + temp
    return temp.rstrip('0')

def check(x, c, idx):
    global ans_list
    imsi, imsi2 = '', []
    if idx < 55:
        return
    
    for i in range(idx, -1, -c):
        imsi += x[i]
        if len(imsi) == 7:
            imsi = imsi[::-1]
            if imsi in pattern:
                imsi2.append(pattern.index(imsi))
                imsi = ''
            else:
                check(x, c+1, idx)
        if len(imsi2) == 8:
            imsi2 = imsi2[::-1]
            if imsi2 not in ans_list:
                ans_list.append(imsi2)
            check(x[:i].rstrip('0'), 1, len(x[:i].rstrip('0'))-1)
            break


pattern = [
    '0001101', '0011001', '0010011', '0111101', '0100011',
    '0110001', '0101111', '0111011', '0110111', '0001011']

TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().strip().split())
    num_arr = []
    ans, ans_list = 0, []
    for _ in range(n):
        a = input().strip().strip('0')
        if a:
            line = binary(a)
            check(line, 1, len(line)-1)

    for i in range(len(ans_list)):
        dap = 0
        for j in range(8):
            if j % 2 == 0:
                dap += (ans_list[i][j] * 3)
            else:
                dap += ans_list[i][j]
        if dap % 10 == 0:
            ans += sum(ans_list[i])
    
    print(f'#{tc} {ans}')