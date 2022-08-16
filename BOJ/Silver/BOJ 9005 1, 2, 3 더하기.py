def hap(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return hap(n-1) + hap(n-2) + hap(n-3)

TC = int(input())

for i in range(TC):
    print(hap(int(input())))

# 재귀식을 구현할 규칙을 빠르게 알아내는게 핵심