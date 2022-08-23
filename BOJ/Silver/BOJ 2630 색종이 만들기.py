import sys
input = sys.stdin.readline


def papercheck(x, y, n):
    global zero, one
    gijun = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != gijun:
                for m in range(2):
                    for l in range(2):
                        papercheck(x+(m*n)//2, y+(l*n)//2, n//2)
                return None

    if gijun == 0:
        zero += 1
    elif gijun == 1:
        one += 1

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

zero, one = 0, 0

papercheck(0, 0, n)

print(zero)
print(one)