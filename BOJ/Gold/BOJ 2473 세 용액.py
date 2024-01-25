import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

ans = 3000000000
ans_i, ans_j, ans_k = 0, 0, 0

for k in range(N-2):
    i, j = k+1, N-1
    while i < j:
        temp = arr[i] + arr[j] + arr[k]

        if ans > abs(temp):
            ans = abs(temp)
            ans_i = i
            ans_j = j
            ans_k = k
            if not ans:
                break
        if temp > 0:
            j -= 1
        else:
            i += 1

print(*sorted([arr[ans_i], arr[ans_j], arr[ans_k]]))
