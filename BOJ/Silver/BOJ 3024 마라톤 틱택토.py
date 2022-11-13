N = int(input())

arr = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j].isalpha():
            if i+2 < N and j+2 < N:
                if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2]:
                    print(arr[i][j])
                    quit()
            if i+2 < N:
                if arr[i][j] == arr[i+1][j] == arr[i+2][j]:
                    print(arr[i][j])
                    quit()
            if j+2 < N:
                if arr[i][j] == arr[i][j+1] == arr[i][j+2]:
                    print(arr[i][j])
                    quit()
            
print('ongoing')