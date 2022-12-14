def choice(k):
    global yumi_x, yumi_y, minV
    if k == 3:
        total.append(selected)
        for a in total:
            distance = 0
            yumi_x, yumi_y = ori_x, ori_y
            for b in a:
                x, y = people[b][0], people[b][1]
                distance += ((x-yumi_x) ** 2 + (y-yumi_y) ** 2) ** 0.5
                yumi_x, yumi_y = x, y
            minV = min(distance, minV)
    else:
        for i in range(3):
            if not visited[i]:
                visited[i] = 1
                selected.append(i)
                choice(k+1)
                visited[i] = 0
                selected.pop()

ori_x, ori_y = map(int, input().split())
yumi_x, yumi_y = ori_x, ori_y
people = [list(map(int, input().split())) for _ in range(3)]
selected = []
visited = [0]*3
total = []
minV = 10**10
choice(0)
print(int(minV))