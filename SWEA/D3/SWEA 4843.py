T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    temp_arr = []
    arr.sort()
    print(f'#{i+1} ', end='')
    for j in range(10):
        if j % 2 == 0:
            print(arr[N-(j//2)-1], '', end='')
        else:
            print(arr[j//2], '', end='')
    print('')


        


