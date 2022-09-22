# 실행시간 152ms


def back(c):
    global cnt
    # 조건 미달시 return
    if c < 0:
        return
     
    # 마지막 날까지 근력 조건을 만족했다면 cnt += 1
    if sum(visited) == n and c >= 0:
        cnt += 1
        return
    
    # 매일 손실분만큼 빼주기
    c -= k
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            # 근력 증가량 더해준 뒤, 재귀 호출
            back(c + arr[i])
            visited[i] = 0
    return cnt



n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
visited = [0]*n

print(back(0))