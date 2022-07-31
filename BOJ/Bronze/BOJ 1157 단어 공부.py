a = input().upper()

b = list(set(a))

cnt_list = []
for i in b:
    count = a.count(i)
    cnt_list.append(count)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')

else:
    print(b[cnt_list.index(max(cnt_list))])