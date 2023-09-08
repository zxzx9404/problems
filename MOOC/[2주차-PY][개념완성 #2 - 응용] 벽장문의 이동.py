N = int(input())
open = sorted(list(map(int, input().split())))
order_num = int(input())
orders = list(int(input()) for _ in range(order_num))

def DFS(s, left, right, sum_move):
    global ans
    if ans <= sum_move:
        return
    if s >= order_num:
        ans = sum_move
        return
   
    if orders[s] < right:
        DFS(s+1, orders[s], right, sum_move + abs(left-orders[s]))
    if left < orders[s]: 
        DFS(s+1, left, orders[s], sum_move + abs(right-orders[s]))
      

ans = 9999999999999
print(open)
DFS(0, open[0], open[1], 0)
   
# 출력하는 부분
print(ans)
