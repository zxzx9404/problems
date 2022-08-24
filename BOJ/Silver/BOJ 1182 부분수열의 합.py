n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1<<n):                  # 1<<n : 부분 집합의 개수
    temp= []
    for j in range(n):                 # 원소의 수 만큼 비트를 비교함
        if i & (1<<j):                 # i의 j번 비트가 1인 경우
            temp.append(arr[j])        # j번 원소를 더함
    if sum(temp) == s and temp != []:
        cnt += 1

print(cnt)