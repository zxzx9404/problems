TC = int(input())
for tc in range(TC):
    num = int(input())
    zero = 1
    one = 0
    for _ in range(num):
        one, zero = one + zero, one
    print(zero, one)

# 몇번 계산해보고 공식 유추