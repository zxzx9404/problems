# 문제가 너무 불친절하게 나와있다..
# 덕분에 식 3번 갈아엎음

## 문제풀이 과정 ## 
'''
1. 0~n-1까지의 숫자를 가진 부분집합에서 n//2개의 원소를 가진 부분집합을 추출
2. 1번에서 찾은 부분집합을 하나씩 순회하면서 해당 인덱스에 해당하는 시너지합을 계산
3. 2번에서 사용하지 않은 인덱스가 나머지 요리를 구성할 것이므로, 나머지 요리의 시너지합 계산
4. 2번과 3번에서 계산된 시너지합의 차이를 구해, 현재의 최소값과 비교
'''



TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # '인덱스 번호 == 값'을 가진 배열, 인덱스값 추출용
    com = [xx for xx in range(n)]
    sel = []
    # n개의 원소 중 n//2개를 추출한 부분집합들을 담는 과정
    for i in range(1<<n):
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp.append(com[j])
            if len(temp) > n//2:
                break
        if len(temp) == n//2:
            sel.append(temp)
    
    # 임의의 큰 값으로 설정
    min_cha = 100000000000000

    # 부분집합 리스트 sel을 순회하며, 1번 요리의 시너지값을 찾는 과정
    for t in sel:
        temp1, temp2 = 0, 0
        for i in range(1<<n//2):
            temp = []
            for j in range(n//2):
                if i & (1<<j):
                    temp.append(t[j])
                if len(temp) > 2:
                    break
            if len(temp) == 2:
                temp1 += arr[temp[0]][temp[1]] + arr[temp[1]][temp[0]]
        
        # sel[t]에 없는 원소들만을 찾아, 2번 요리의 시너지값을 찾는 과정
        tt = []
        for i in range(n):
            if i not in t:
                tt.append(i)
        for i in range(1<<n//2):
            temp = []
            for j in range(n//2):
                if i & (1<<j):
                    temp.append(tt[j])
                if len(temp) > 2:
                    break
            if len(temp) == 2:
                temp2 += arr[temp[0]][temp[1]] + arr[temp[1]][temp[0]]
        
        # 시너지값 비교
        min_cha = min(min_cha, abs(temp1-temp2))        
                
                
    print(f'#{tc} {min_cha}')