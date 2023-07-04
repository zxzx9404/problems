# itertools를 이용한 구현 pypy 메모리초과 / python 3516ms

from itertools import permutations

N = int(input())
sign = list(input().split())
max_ans, min_ans = '0', '9999999999'

temps = list(permutations(range(10), N+1))

for temp in temps:
    idx = 0
    flag = True
    while flag and idx < N:
        if sign[idx] == '<' and temp[idx] >= temp[idx+1]:
            flag = False
        elif sign[idx] == '>' and temp[idx] <= temp[idx+1]:
            flag = False
        idx += 1
    
    if flag:
        number = ''.join(map(str, temp))
        if int(max_ans) < int(number):
            max_ans = number
        if int(min_ans) > int(number):
            min_ans = number

print(max_ans)
print(min_ans)


'''
강의


모든 경우의 수를 확인할 경우의 시간 복잡도
2^(k+1) * (k+1)! * (k+1)

아래와 같은 로직의 시간 복잡도
(k+1)! * (k+1)




제일 큰 수, 제일 작은 수만 구하는 것이기 때문에 모든 경우의 수를 해 볼 필요가 없다.

ex) 부등호가 3개라면
- 숫자는 4개가 필요할 것이고,
- 제일 큰 수는 6 7 8 9를 사용한 수, 제일 작은 수는 0 1 2 3을 사용한 숫자가 될 것이다.

- 제일 작은 수를 찾는 방법은 0123이 조건에 맞는지 확인 -> 아니라면 0132 -> 아니라면 0213 등 점점 커지는 순서대로 확인
- 하나라도 찾으면 그게 최솟값이므로 바로 break

- 제일 큰 수를 찾는 것은 9876부터 시작하여 점점 내려감(로직은 제일 작은 수 찾는 것과 같음)
'''