### 접근 아이디어(팰린드롬이 가능한 조건) ###
# 단어의 길이가 짝수라면, 모든 알파벳들이 짝수개로 존재해야 한다.
# 단어의 길이가 홀수라면, 한 알파벳만 홀수개 / 나머지는 짝수개 존재해야 함
# 위의 조건을 통과했다면 팰린드롬이 가능한 것이므로 사전 순으로 만들어주면 끝

# 68ms


word = list(input())
word_dct = {}  # 알파벳을 key로, 개수를 value로 가지는 딕셔너리
p = False

for i in word:
    word_dct[i] = word_dct.get(i, 0) + 1

word_dct = dict(sorted(word_dct.items()))  # 알파벳 순서로 sort

if len(word) % 2:  # 길이가 홀수
    for key in word_dct:
        if word_dct[key] % 2:
            if not p:
                p = True
            else:
                print("I'm Sorry Hansoo")  # 홀수개인 알파벳이 2개 이상 나오면 팰린드롬 불가
                quit()    

else:  # 길이가 짝수
    for key in word_dct:
        if word_dct[key] % 2:  # 홀수개인 알파벳이 있다면 팰린드롬 불가
            print("I'm Sorry Hansoo")
            quit()


ans = idx = ''

# 회문이기 때문에, 반쪽짜리 정답을 만들어주고 반대로 이어서 붙임
for key in word_dct:
    if word_dct[key] >= 2:
        ans += key*(word_dct[key]//2)
    if word_dct[key] % 2:
        idx = key

print(ans+idx+ans[::-1])