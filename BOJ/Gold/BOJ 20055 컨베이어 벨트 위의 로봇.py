N, K = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(2*N):
    arr[i] = [arr[i], 0]

step = 0
stop = 0

# 내리는 위치에 로봇 있으면 없애는 함수
def get_out():
    if arr[N-1][1]:
        arr[N-1][1] = 0

# 종료여부 판단
def finished():
    if stop >= K:
        print(step)
        quit()

while True:
    step += 1

    # 스텝 1 : 벨트의 회전
    arr.insert(0, arr.pop())
    get_out()
    
    # 스텝 2 : 로봇의 이동
    new_arr = arr[:]
    for i in range(N-1, -1, -1):
        if arr[i][1]:
            next = i+1 if i < 2*N-1 else 0
            if not arr[next][1] and arr[next][0]:
                new_arr[next][0] -= 1
                new_arr[next][1] = 1
                arr[i][1] = 0
                if not new_arr[next][0]:
                    stop += 1
                
    arr = new_arr
    get_out()
    
    # 스텝 3 : 로봇을 올림
    if arr[0][0] and not arr[0][1]:
        arr[0][0] -= 1
        arr[0][1] = step
        if not arr[0][0]:
            stop += 1
    get_out()
    
    if step <= 10:
        print(arr[0:N])
        print(arr[N:])
        print(step)
        print()
    

    
    # 스텝 4 : 종료 여부 판단
    finished()