N = int(input())
ans = 0

for _ in range(N):
    word = input()
    stk = []
    for i in word:
        if stk and stk[-1] == i:
            stk.pop()
        else:
            stk.append(i)
    if not stk:
        ans += 1

print(ans)