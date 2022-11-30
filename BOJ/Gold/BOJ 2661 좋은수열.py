def check_same(cnt, num):    
    for i in range(1, cnt//2+1):
        if num[-i:] == num[-i*2:-i]:
            return True
    return False

def backtrace(cnt, num):
    
    if check_same(cnt, num):
        return

    if cnt == N:
        print(num)
        quit()
    
    backtrace(cnt + 1, num + '1')
    backtrace(cnt + 1, num + '2')
    backtrace(cnt + 1, num + '3')
    

N = int(input())

backtrace(0, '')
