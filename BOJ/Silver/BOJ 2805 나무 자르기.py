import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))



bottom, top = 0, max(arr)
while bottom <= top:
    namu = 0
    mid = (bottom + top) // 2
    for i in arr:
        if namu > m:
            break
        else:
            if i - mid > 0:
                namu += i - mid
    if namu >= m:
        bottom = mid + 1
    else:
        top = mid - 1
print(top)


# 1654번 랜선 자르기와 완전히 동일한 문제이나
# 음수가 나올 경우 더해주지 않아야 함