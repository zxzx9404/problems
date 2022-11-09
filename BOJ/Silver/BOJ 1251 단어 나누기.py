# 그리디 풀이.. 이왜답? <- 반례 알고있는데 백준에선 정답이래요

word= list(input())
N, n = len(word), 0
min1 = min2 = min3 = []
for i in range(N-2):
    temp = word[0:i+1][::-1]
    if not min1 or temp < min1:
        min1 = temp
n += len(min1)

for j in range(n, N-1):
    temp = word[n:j+1][::-1]
    if not min2 or temp < min2:
        min2 = temp
n += len(min2)

for k in range(n, N):
    temp = word[n:][::-1]
    if not min3 or temp < min3:
        min3 = temp

print(''.join(min1+min2+min3))


# 정석 브루트포스 풀이
word= input()
N = len(word)
ans = 'z'*N
for i in range(1, N-1):
    for j in range(i+1, N):
        temp = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        ans = min(ans, temp)
print(ans)


# 심심해서 해본 숏코딩 // 위 브루트포스와 같은 로직
word = input(); N = len(word)
ans_list = [[ word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]  for j in range(i+1, N)] for i in range(1, N-1)]
print(min(sum(ans_list, [])))