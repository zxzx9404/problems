x, y = map(int, input().split())
a = int(input())
jari_x = 1
jari_y = 0

if x*y < a:
    print(0)
else:
    count = 0
    direction = 'y'
    turn_x = 0
    turn_y = 0
    for i in range(a):
        if direction == 'y':
            count += 1
            if turn_y % 2 == 0:
                jari_y += 1
            else:
                jari_y -= 1
            if count == y-turn_y:
                direction = 'x'
                count = 0
                turn_y += 1
        elif direction == 'x':
            count += 1
            if turn_x % 2 == 0:
                jari_x += 1
            else:
                jari_x -= 1
            if count == x-turn_x-1:
                direction = 'y'
                count = 0
                turn_x += 1
    print(jari_x, jari_y)