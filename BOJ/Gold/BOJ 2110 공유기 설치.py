def check(m):
    cnt = C - 1
    now = house[0]
    
    for i in range(1, N):
        if house[i] >= now + m:
            cnt -= 1
            if not cnt:
                return True
            now = house[i]
    return False

N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])

s, e = 1, house[-1] // (C-1)

while s <= e:
    m = (s + e) // 2
    if check(m):
        s = m + 1
    else:
        e = m - 1

print(s-1)
