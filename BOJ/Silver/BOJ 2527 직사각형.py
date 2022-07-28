for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    xa, xb, ya, yb = max(x1, x2), min(p1, p2), max(y1, y2), min(q1, q2)

    chai_x = xb - xa
    chai_y = yb - ya

    if chai_x > 0 and chai_y > 0:
        print('a')
    elif chai_x < 0 and chai_y < 0:
        print('d')
    elif chai_x == 0 and chai_y == 0:
        print('c')
    else:
        print('b')