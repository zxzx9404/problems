TC = int(input())

for tc in range(1, TC+1):
    A, B = input().split()
    ans = len(A)               # 한번도 겹치지 않은 경우를 정답으로 가정
    i, j, temp = 0, 0, 0
    while i <= len(A)-len(B):
        if A[i+j] == B[j]:     # 문자열 한글자씩 비교
            temp += 1
            j += 1
        else:                  # 다르다면 나머지 변수 초기화 후 한칸 전진
            i += 1
            j = 0
            temp = 0
        if temp == len(B):     # 일치하는 문자열을 찾았다면
            ans -= len(B)-1    # B의 글자수 -1번을 줄여줌
            j = 0              # B의 인덱스 초기화
            i += len(B)        # 찾은 글자수 만큼은 더이상 검사할 필요 없으니 점프
            temp = 0
    print(f'#{tc} {ans}')
        
        