TC = int(input())

for tc in range(1, TC+1):
    A = input()
    B = input()             
    i, j, temp = 0, 0, 0
    p = False
    while i <= len(B)-len(A):
        if B[i+j] == A[j]:     # 문자열 한글자씩 비교
            temp += 1
            j += 1
        else:                  # 다르다면 나머지 변수 초기화 후 한칸 전진
            i += 1
            j = 0
            temp = 0
        if temp == len(A):     # 일치하는 문자열을 찾았다면
            p = True           # 변수를 True로 바꾸고
            break              # break
    if p:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')