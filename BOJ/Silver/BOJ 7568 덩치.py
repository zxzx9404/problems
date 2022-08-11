TC = int(input())

arr = []
arr2 = []
for _ in range(TC):
    a, b= map(int, input().split())
    arr.append(a)
    arr2.append(b)

wei = sorted(list(set(arr)))
hei = sorted(list(set(arr2)))

print(wei, hei)