from collections import deque

n = int(input())
list_card = deque()

for i in range(1, n+1):
    list_card.append(i)
    
while len(card) > 1:
    list_card.popleft()
    list_card.append(list_card.popleft())

print(list_card[0])

'''
deque 개념 학습 없이 짜본 코드.
코드는 맞는것 같은데 역시나 시간초과

n = int(input())
list_a = []
list_b = []

for i in range(1, n+1):
    list_a.append(i)
    

while True:
    if list_a == [] and len(list_b) == 1:
        print(list_b[0])
        break
    elif list_b == [] and len(list_a) == 1:
        print(list_a[0])
        break
    for i in range(len(list_a)//2):
        del list_a[0]
        list_b.append(list_a.pop(0))
    if list_a != [] and len(list_b) != 0:
        del list_a[0]
        list_a.append(list_b.pop(0))
    for i in range(len(list_b)//2):
        del list_b[0]
        list_a.append(list_b.pop(0))
    if list_b != [] and len(list_a) != 0:
        del list_b[0]
        list_b.append(list_a.pop(0))
'''

