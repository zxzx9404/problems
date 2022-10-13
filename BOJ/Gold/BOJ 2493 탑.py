N = int(input())
arr = list(map(int, input().split()))
ans = [0]*N

stk = []
# 첫 번째 타워의 높이, 인덱스 번호를 스택에 넣고 시작
stk.append((arr[0], 0))

idx = 1
while idx < N:
    # 스택의 마지막 원소보다 작다면
    if arr[idx] < stk[-1][0]:
        # 그 원소에게 레이저가 막히는 것이므로 원소번호 답에 저장하고 스택에 push
        ans[idx] = stk[-1][1]+1
        stk.append((arr[idx], idx))
    else:
        # 스택의 마지막 인자보다 크다면, 자신의 레이저를 막아줄 원소가 나올때까지 pop 후 push
        while stk and arr[idx] >= stk[-1][0]:
            stk.pop()
        # 만약 누군가한테 막혔다면, 그 원소번호를 저장
        if stk:
            ans[idx] = stk[-1][1]+1
        stk.append((arr[idx], idx))

    idx += 1
    
print(*ans)