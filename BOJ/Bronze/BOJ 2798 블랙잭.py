a, b = map(int, input().split())
list_card = list(map(int, input().split()))
max = 0

for i in range(a):
    for j in range(a):
        for k in range(a):
            if i == j or i == k or j == k:
                continue
            else:
                if list_card[i]+list_card[j]+list_card[k] > b:
                    continue
                elif list_card[i]+list_card[j]+list_card[k] > max:
                    max = list_card[i]+list_card[j]+list_card[k]
print(max)