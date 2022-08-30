L, C = map(int, input().split())
arr = input().split()

# 모음 집합 만들기
vowel = []

# 필요한 모음 추가
for i in arr:
    if i in 'aeiou':
        vowel.append(i)


# 정답이 담길 리스트
ans = []

# 부분집합 생성
for i in range(1<<C):
    temp = []
    for j in range(C):
        if i & (1<<j):
            temp.append(arr[j])
        # 가지치기, 길이가 L을 초과하면 break
        if len(temp) > L:
            break
    # 길이가 L 일경우
    if len(temp) == L:
        cnt = 0
        # 모음의 개수 세주기
        for k in vowel:
            for u in temp:
                if k == u:
                    cnt += 1
        # 모음이 1개 이상, 자음이 2개 이상인 경우의 조건식
        if 0 < cnt <= L - 2:
            # sort 후 하나의 문자열로 합쳐서 정답에 추가
            ans.append(''.join(sorted(temp)))
# 정렬
ans.sort()
            
# 양식에 맞게 출력
for i in ans:
    print(i)
