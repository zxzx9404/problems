# 스택에 여러개를 담아 놓을 필요가 없고, 하나만 담기면 됨
# 어려운 문제는 아니었으나, 변수의 위치를 다르게 적어서 틀림..

for tc in range(1, 11):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N):
        stk = []
        for j in range(N):
            if not stk and arr[j][i] == 1:
                stk.append(1)    
            elif arr[j][i] == 2 and stk:
                stk.pop()
                cnt += 1
    print(f'#{tc} {cnt}')