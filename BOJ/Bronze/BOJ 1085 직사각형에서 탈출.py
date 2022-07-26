x, y, w, h = map(int, input().split())

range_list = [x, (w-x), y, (h-y)]

print(min(range_list))