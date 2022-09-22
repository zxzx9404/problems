dankey = [] 

n = int(input())

for _ in range(n):
    word = input().split()
    # 첫 글자 먼저 탐색
    for i in range(len(word)):
        # 현재 단어의 첫 글자가 단축기로 지정되어 있지 않다면
        if word[i][0].upper() not in dankey:
            # 단축키 목록에 추가한 후 괄호로 감싸 출력
            dankey.append(word[i][0].upper()) 
            word[i] = "[" + word[i][0] + "]" + word[i][1:] 
            print(' '.join(word))
            break

    # 첫 글자를 단축키로 지정하지 못했다면
    else:
        for j in range(len(word)):
            # 반복문 탈출용 변수 p
            p = False
            for k in range(len(word[j])):
                # 현재 단어의 알파벳이 단축기로 지정되어 있지 않다면
                if word[j][k].upper() not in dankey:
                    # 단축키 목록에 추가한 후 괄호로 감싸 출력
                    dankey.append(word[j][k].upper())
                    word[j] = word[j][:k] + "[" + word[j][k] + "]" + word[j][k + 1:] 
                    print(' '.join(word))
                    # 반복문 탈출용 변수값 변경
                    p = True
                    break
            if p:
                break

        # 단축키 지정에 실패한 경우 그냥 출력
        else:
            print(*word)