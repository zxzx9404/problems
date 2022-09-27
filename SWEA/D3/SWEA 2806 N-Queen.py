def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    ans = 0
    row = [0] * n
    n_queens(0)
    print(f'#{tc} {ans}')