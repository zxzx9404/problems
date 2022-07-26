ham = []
bev = []
for i in range(3):
    temp_ham = int(input())
    ham.append(temp_ham)
for i in range(2):
    temp_bev = int(input())
    bev.append(temp_bev)

print(min(ham)+min(bev)-50)