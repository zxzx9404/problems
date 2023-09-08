def M1(c, arr):
    if c == N:
        print(*arr)
        return
    
    for i in range(1, 7):
        M1(c+1, arr + [i])


def M2(c, arr, ex):
    if c == N:
        print(*arr)
        return
    
    for i in range(ex, 7):
        M2(c+1, arr + [i], i)


def M3(c, arr):
    if c == N:
        print(*arr)
        return
    
    for i in range(1, 7):
        if not using[i]:
            using[i] = 1
            M3(c+1, arr + [i])
            using[i] = 0


N, M = map(int, input().split())

using = [0]*7


if M == 1:
    M1(0, [])
elif M == 2:
    M2(0, [], 1)
elif M == 3:
    M3(0, [])
