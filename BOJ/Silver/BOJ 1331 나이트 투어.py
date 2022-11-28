start = input()
sti, stj = ord(start[0]), int(start[1])
route_list = [[sti, stj]]

for _ in range(35):
    route = input()
    A, N = ord(route[0]), int(route[1])

    if ((abs(sti - A) == 2 and abs(stj - N) == 1) or (abs(sti - A) == 1 and abs(stj - N) == 2)) and [A, N] not in route_list:
        route_list.append([A, N])
        sti, stj = A, N
    else:
        print('Invalid')
        exit()   


if (abs(route_list[0][0] - A) == 2 and abs(route_list[0][1] - N) == 1) or (abs(route_list[0][0] - A) == 1 and abs(route_list[0][1] - N) == 2):
    print('Valid')
else:
    print('Invalid')