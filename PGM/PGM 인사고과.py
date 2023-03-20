'''
### 첫번째 생각

- x가 제일 큰 사람 중에서 y가 제일 큰 애 (x_top)
- y가 제일 큰 사람 중에서 x가 제일 큰 애 (y_top)

 이렇게 2명을 뽑은다음, 둘 중 한명보다라도 작으면 탈락시킴.

→ 살아남으면 완호랑 합 비교

정답률 : 19/25

반례 : [[3,2], [2,5], [5,2], [4,3]]

x탑은 5,2

y탑은 2,5

이 둘이랑 비교하면 완호가 살아남지만, 4,3 때문에 탈락해야하는걸 못잡아냄

### 두번째 생각

- lambda x : (x[0], x[1]), reverse=True 로 정렬하고
- scores[0]을 기준으로잡고
- scores[0][0] 보다 x가 작고, scores[0][1]보다 y가 작다면 탈락

→ 살아남으면 완호랑 합 비교

정답률 : 18/25

반례 : [[2,2], [5,2], [3,3]]

5,2가 기준인데, 얘랑 비교하면 완호는 살지만, 3,3이랑 비교하면 탈락인데 그걸 못잡아냄

### 세번째 생각

- lambda x : (x[0], -x[1]), reverse=True 로 정렬하고
- 완호는 매번 비교해서 탈락여부 확인
- x는 첫 사람이 제일 크니까 y만 쭉 비교하면서 직전 max_y보다 커야 살아남음

→ 살아남으면 완호랑 합 비교

정답률 : 25/25

profit!
'''

def solution(scores):
    answer = 1
    wan = scores[0]
    scores = sorted(scores, key=lambda x : (x[0], -x[1]), reverse=True)
    gijun = scores[0][1]
    for i, j in scores:
        if wan[0] < i and wan[1] < j:
            return -1
        if gijun <= j:
            if sum(wan) < (i+j):
                answer += 1
            gijun = j
    
    return answer