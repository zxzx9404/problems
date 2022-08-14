import sys
input = sys.stdin.readline


TC = int(input())

arr = []

for tc in range(TC):
    a = list(input().split())
    if a[0] == 'add' and a[1] not in arr:
        arr.append(a[1])
    if a[0] == 'remove' and a[1] in arr:
        del arr[arr.index(a[1])]
    if a[0] == 'check':
        if a[1] in arr:
            print(1)
        else:
            print(0)
    if a[0] == 'toggle':
        if a[1] in arr:
            del arr[arr.index(a[1])]
        elif a[1] not in arr:
            arr.append(a[1])
    if a[0] == 'all':
        arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    if a[0] == 'empty':
        arr= []
        
# 리스트로도 풀렸지만, 다른분들의 풀이를 보니 set으로 풀라고 한 문제 같음
# set의 메서드인 add와 discard에 대해 알아놓기(둘다 시간복잡도 O(1))