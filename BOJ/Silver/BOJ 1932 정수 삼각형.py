# 리프노드 바로 윗 줄부터 시작. 각 노드에서, 자신의 자식노드 중 큰 값을 취함
# 루트까지 반복 후, 루트값 출력 

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-2, -1, -1):
    for j in range(i+1):
        arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])

print(arr[0][0])