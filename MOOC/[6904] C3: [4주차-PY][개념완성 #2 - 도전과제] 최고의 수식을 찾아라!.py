N = int(input())

wi = list(map(int, input().split()))
vi = list(map(int, input().split()))
ai = int(input())

set = [1, 2, 4, 8, 16, 32, 64]
chk = [0]* 7

value = 0
sol = 0
s = [0]* 7

def checkHang():
    ret = 0
    for i in range(7):
        ret += chk[i]
    return ret

def DFS(n, sum):
    global value, sol
    if sum > N:
        return

    if sum == N:
        value = 0
        for k in range(7):
            if chk[k]>= 5:
                value += (chk[k]* vi[k])
            else:
                value += (chk[k]* wi[k])
        value += (ai * checkHang())

        if value > sol:
            sol = value
            for l in range(7):
                s[l]= chk[l]
        return

    for i in range(n, 7):
        chk[i]+= 1
        DFS(i, sum + set[i])
        chk[i]-= 1

DFS(0, 0)

print(sol)
for i in range(7):
    print(s[i], end=' ')
