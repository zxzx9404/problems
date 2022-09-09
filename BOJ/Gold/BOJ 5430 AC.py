# 차근차근 하나씩 구현함

from collections import deque

TC = int(input())

for _ in range(TC):
    AC = input()
    n = int(input())
    a = input()
    arr = deque()
    # 빼내는 행위(D)가 숫자의 개수보다 많다면 바로 error 출력
    if n < AC.count('D'):
        print('error')
    else:
        # [1,2,3] 형태의 입력을 분리하여 숫자만 받는 과정
        temp = ''
        for i in a:
            if i.isnumeric():
                temp += i
            elif i  == ',':
                arr.append(temp)
                temp = ''
        if temp != '':
            arr.append(temp)
        cnt = 0
        ans = ''
        for i in AC:
            # R 이 한번 나올때마다 빼내는 위치가 맨앞 <-> 맨뒤 순환
            if i == 'R':
                cnt += 1
            else:
                if cnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
        # 마지막으로 바라보고 있는 위치에 따라 순서대로 빼줌
        if cnt % 2 == 0:
            while len(arr) != 0:
                ans += arr.popleft()
                ans += ','
        else:
            while len(arr) != 0:
                ans += arr.pop()
                ans += ','
        # []를 더해주는 과정
        ans = ans[:len(ans)-1]
        ans = '[' + ans
        ans += ']'
        print(ans)