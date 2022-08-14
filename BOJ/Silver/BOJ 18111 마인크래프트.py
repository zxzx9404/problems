import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

idx = 0
ans = 100000000000000
for tc in range(257):
    have_b, use_b = 0, 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= tc:
                have_b += arr[i][j] - tc
            else:
                use_b += tc - arr[i][j]
    
    if have_b + B >= use_b:
        temp = have_b * 2 + use_b
        if ans >= temp:
            ans = temp
            idx = tc
print(ans, idx)

# python 3으로 제출시 시간초과가 떠서
# PyPy3 으로 제출
# python 으로 해결하는 방법은 몰?루