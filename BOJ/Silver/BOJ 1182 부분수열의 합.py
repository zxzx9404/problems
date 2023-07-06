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

'''
- 23/07/06 추가 풀이

def dfs(index, sum_of_num, flag):
    global cnt
    
    if flag and sum_of_num == S:
        cnt += 1
        
    if index == N:
        return

    dfs(index+1, sum_of_num, False)
    dfs(index+1, sum_of_num + arr[index], True)
    

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
dfs(0, 0, False)
print(cnt)

- 전체 부분집합을 구하지 않고, 재귀 호출을 통해 값만 확인하는 방식
- 기존 코드 대비 시간 대폭 감소 3640ms -> 252ms

'''
