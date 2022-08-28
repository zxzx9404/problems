# 실제 작업을 수행하지 않고, 수학적으로 접근

TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = m % n
    print(f'#{tc} {arr[idx]}')

