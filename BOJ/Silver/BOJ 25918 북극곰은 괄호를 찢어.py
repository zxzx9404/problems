# 132ms
# 문제의 조건대로 하루하루 시뮬레이션을 돌리면 최대 100000일까지의 탐색이 필요
# 완탐을 10만번 돌리면 시초남 (== 한번의 탐색으로 모든걸 끝내야함)
# '()' 짝 맞춰 빼는 문제들 기존에 풀때 stack으로 푸는게 제일 효율적이었으므로 stack으로 접근
# 완성된 괄호 모양을 시작점으로 놓고 거꾸로 탐색해나가 시작 날짜(빈 상태)까지 가는데 걸리는 시간을 구함
# 스택에 N개의 괄호가 쌓이면 해당 괄호쌍을 완성하는데는 N일이 걸린다는 뜻이므로 
# 스택의 순간 최대 길이가 곧 필요한 날짜가 된다.


N = int(input())
word = input()
cnt = 0
stk = []

for i in word:
    if not stk:                        # 비었으면 push
        stk.append(i)
    elif stk[-1] == '(' and i == ')':  # 'O'쌍이면 pop
        stk.pop()
    elif stk[-1] == ')' and i == '(':  # 'X'쌍이면 pop
        stk.pop()
    else:                              # 둘다 아니면 push
        stk.append(i)
   
    cnt = max(cnt, len(stk))           # 스택의 최대길이 == 답

if stk:  # 해당 형태 완성 불가
    print(-1)
else:    # 완성 가능
    print(cnt)





################ 하루하루 시뮬돌리는 코드(시간초과)
# N = int(input())
# today = list(map(str, input()))
# cnt = 0

# if N == 1:
#     print(-1)
#     quit()

# while True:
#     st = today[:]
#     idx = 0
#     while idx < len(today)-1:
#         if today[idx] == '(' and today[idx+1] == ')':
#             today.pop(idx), today.pop(idx)
#         elif today[idx] == ')' and today[idx+1] == '(':
#             today.pop(idx), today.pop(idx)
#         else:
#             idx += 1
#     cnt += 1
#     if not today:
#         print(cnt)
#         break
#     if st == today:
#         print(-1)
#         break