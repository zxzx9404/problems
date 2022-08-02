a, b= map(int, input().split())
n = int(input())
cut_x = [0, b]
cut_y = [0, a]

for _ in range(n):
    c, d = map(int, input().split())
    if c == 0:
        cut_x.append(d)
    else:
        cut_y.append(d)

cut_x.sort()
cut_y.sort()

temp_x = 0
temp_y = 0
for i in range(len(cut_x)-1):
    if cut_x[i+1]-cut_x[i] >= temp_x:
        temp_x = cut_x[i+1]-cut_x[i]

for i in range(len(cut_y)-1):
    if cut_y[i+1]-cut_y[i] >= temp_y:
        temp_y = cut_y[i+1]-cut_y[i]


print(temp_x*temp_y)       

