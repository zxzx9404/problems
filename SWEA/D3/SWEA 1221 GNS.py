TC = int(input())

for tc in range(TC):
    a, b = input().split()
    arr2 = [['ZRO', 0], ['ONE', 0], ['TWO', 0], ['THR', 0], ['FOR', 0], ['FIV', 0], ['SIX', 0], ['SVN', 0], ['EGT', 0], ['NIN', 0]]
    arr = list(map(str, input().split()))
    for i in arr:
        for j in range(10):
            if i == arr2[j][0]:
                arr2[j][1] += 1
    print(a)
    for k in range(10):
        for l in range(arr2[k][1]):
            print(arr2[k][0], end=' ')