def far(dir, i):
    if dir == dong[0]: # 같은 줄
        return abs(i - dong[1])
    elif dir + dong[0] == 3 or dir + dong[0] == 7: # 동서 서동 남북 북남
        if dir + dong[0] == 3:
            return N + min(i+dong[1], M-i+M-dong[1])
        elif dir + dong[0] == 7:
            return M + min(i+dong[1], N-i+N-dong[1])
    else:
        if dir + dong[0] == 4: # 서북 북서
            return dong[1] + i
        elif dir + dong[0] == 5: # 서남 남서 북동 동북
            if dong[0] == 1 or dong[0] == 3:
                return N-dong[1] + i
            elif dong[0] == 2 or dong[0] == 4:
                return dong[1] + N-i
        elif dir + dong[0] == 6: # 남동 동남
            if dong[0] == 2:
                return M-dong[1] + N-i
            else:
                return N-dong[1] + M-i


M, N = map(int, input().split())

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dong = list(map(int, input().split()))

ans = 0

for dir, i in arr:
    ans += far(dir, i)

print(ans)