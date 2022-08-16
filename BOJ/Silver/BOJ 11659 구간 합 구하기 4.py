import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [0]
sum = 0
for i in arr:
    sum += i
    arr2.append(sum)


for _ in range(M):
    a, b = map(int, input().split())
    print(arr2[b]-arr2[a-1])

# 시간복잡도가 과다할 경우, prefix_sum 즉 미리 구간합을 계산해놓은 arr를 미리 만들기