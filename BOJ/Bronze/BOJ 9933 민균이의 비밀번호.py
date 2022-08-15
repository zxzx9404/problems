N = int(input())

arr = [] 
p = True
for _ in range(N):
    a = input()
    arr.append(a)
    if a == a[::-1]:
        print(len(a), a[len(a)//2])
        p = False

if p:
    for i in range(N):
        for j in range(N):
            if arr[i] == arr[j][::-1]:
                ans = arr[i]
    print(len(ans), ans[len(ans)//2])