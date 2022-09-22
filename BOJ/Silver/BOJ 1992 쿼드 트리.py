def quad(n, y, x):
    global ans
    # 첫 칸을 기준으로 잡음
    gijun = arr[y][x]
    p = False
    for i in range(y, y+n):
        for j in range(x, x+n):
            # 기준과 다른 칸이 하나라도 나올 시
            if arr[i][j] != gijun:
                p = True
                # 한번의 재귀당 '('과 ')'가 한번씩 필요함
                ans += '('
                # 4개의 재귀문을 수행
                for k in range(2):
                    for m in range(2):
                        quad(n//2, y+n//2*k, x+n//2*m)
                # 한번의 재귀당 '('과 ')'가 한번씩 필요함
                ans += ')'
                break
        if p:
            break
    else:
        # 정상적으로 for문을 탈출한 경우, 모든 숫자가 같은 것이므로 정답에 추가
        ans += str(gijun)
    


n = int(input())
ans = ''
arr = [list(map(int, input())) for _ in range(n)]

quad(n, 0, 0)
print(ans)