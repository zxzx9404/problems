# brute-force식 탐색으로는 시간내에 답을 도출할 수 없음
# 탐색하려는 문자열이 IOIOI의 반복이라는 점을 이용하여 한번의 탐색에 모든 경우를 찾아야 함

n, m, s = int(input()), int(input()), input()

cnt, t, ans = 0, 0, 0
# now[t] 형태로 현재 나타나야 할 패턴을 구분
now = ['I', 'O']

cnt = 0
for i in range(m):
    if s[i] == now[t]:
        cnt += 1
        t = (t + 1) % 2
    else:
        if s[i] == 'I':
            cnt = 1
            t = 1
        else:
            cnt = 0
            t = 0
    if cnt == n*2+1:
        ans += 1
        cnt -= 2
print(ans)