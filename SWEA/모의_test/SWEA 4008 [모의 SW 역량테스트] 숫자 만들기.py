def dfs(cnt, temp):
    global max_ans, min_ans
    if cnt == N:
        max_ans = max(max_ans, temp)
        min_ans = min(min_ans, temp)
        return

    for i in range(4):
        if lst[i] < code[i]:
            lst[i] += 1
            # + - * / 순
            if i == 0:
                dfs(cnt+1, temp + nums[cnt])
            elif i == 1:
                dfs(cnt+1, temp - nums[cnt])
            elif i == 2:
                dfs(cnt+1, temp * nums[cnt])
            elif i == 3:
                if temp < 0 and temp % nums[cnt] != 0:
                    dfs(cnt+1, (temp // nums[cnt]) + 1)
                else:
                    dfs(cnt+1, temp // nums[cnt])
            lst[i] -= 1

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    code = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    lst = [0, 0, 0, 0]
    max_ans = -1000000000
    min_ans = 10000000000
    dfs(1, nums[0])
    print(f'#{tc} {max_ans-min_ans}')