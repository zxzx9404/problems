'''
최신 패션 트렌드가 가죽에 세 개의 점이 있는 암소라고 들은 농부 존은 세 개의 점이 있는 암소를 대량으로 구매를 했다. 불행하게도, 패션 트렌드가 빠르게 변해서 가장 인기 있는 현재 패션은 점이 하나 있는 암소이다.
 
존은 자신의 암소들을 현재 패션 트렌드에 맞게 바꾸고 싶다. 그래서 세 개의 점에 색을 칠해서 한 개의 점으로 만들려고 한다.
예를 들어 암소의 가죽이 N(세로) * M(가로) 크기의 격자로 아래와 같이 주어졌을 때:
 
................
..XXXX....XXX...
...XXXX....XX...
.XXXX......XXX..
........XXXXX...
..XXX....XXX....
 
여기서 각각의 ‘X’는 점의 일부를 나타낸다. 두 ‘X’가 같은 점으로 취급되는 경우는 상하나 좌우로 연결되어 있을 때 이다. 대각선으로 연결된 것은 같은 점으로 보지 않는다. 그래서 위 그림은 정확히 세 점이다. 농부 존의 모든 암소는 정확히 세 점을 가지고 있다.
 
존은 세 점을 한 점으로 만들 때 최대한 적게 색칠하고 싶다. 위의 예에서 그는 4군데에 새로운 ‘X’를 추가하면 된다. (새로운 ‘X’는 ‘*’로 대체해서 쉽게 볼 수 있게 했다. 아래 그림 참조)
 
................
..XXXX....XXX...
...XXXX*...XX...
.XXXX..**..XXX..
...*....XXXXX...
..XXX....XXX....
 
당신이 할 일은 농부 존이 세 개의 점을 병합해서 하나의 큰 점을 만들 수 있게 새로운 ‘X’의 최소 수를 정할 수 있게 도와주는 것이다.
'''

import sys
from collections import deque
import math
   
def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int,readl().split())
    map_leather = [['.']+list(readl().strip())+['.'] if 1<=r<=R else ['.']*(C+2) for r in range(R+2)]
    return R, C, map_leather
   
def Flood_Fill(r, c, num):
    d = ((0,1),(0,-1),(1,0),(-1,0))
    deque_pos = deque()
    q = deque()
    map_leather[r][c] = str(num)
    q.append((r,c))
   
    while q:
        r, c = q.popleft()
        flag = 0
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if map_leather[nr][nc] == '.':
                if flag == 0:
                    flag = 1
                    deque_pos.append((r, c))
            elif map_leather[nr][nc] == 'X':
                map_leather[nr][nc] = str(num)
                q.append((nr, nc))
    return deque_pos
   
def Get_Pos_X(map_leather):
    num = 1
    pos_X = {}
    for r in range(1,R+1):
        for c in range(1,C+1):
            if map_leather[r][c] == 'X':
                deque_pos = Flood_Fill(r, c, num)
                pos_X[num] = deque_pos
                num+=1
    return pos_X
   
def Get_Min_Dist(pos_X):
    min_dist = []
    for n1, n2 in [(1,2),(1,3),(2,3)]:
        min_dist.append(math.inf)
        for r1, c1 in pos_X[n1]:
            for r2, c2 in pos_X[n2]:
                dist = int(abs(r1-r2)) + int(abs(c1-c2))
                if min_dist[-1] > dist:
                    min_dist[-1] = dist
    return min_dist
   
   
   
def GetMin(r,c,deque_pos):
    min_dist = math.inf
    for rr, cc in deque_pos:
        dist = int(abs(r-rr)) + int(abs(c-cc))
        if min_dist > dist: min_dist = dist
    return min_dist-1
   
def Get_Min_Dist2(pos_X, map_leather):
    min_dist = math.inf
    for r in range(1, R+1):
        for c in range(1, C+1):
            if map_leather[r][c] != '.': continue
            dist = GetMin(r,c,pos_X[1])
            dist += GetMin(r,c,pos_X[2])
            dist += GetMin(r,c,pos_X[3])
            if min_dist > dist: min_dist = dist
    return min_dist+1
   
def Solve():
    # 3개의 영역 구분하기
    pos_X = Get_Pos_X(map_leather)
   
    min_dist = Get_Min_Dist(pos_X)
    sol = sum(sorted(min_dist)[:2])-2
   
    min_dist2 = Get_Min_Dist2(pos_X, map_leather)
    if sol > min_dist2: sol = min_dist2
   
    return sol
   
 
sol = -1
 
# 입력 받는 부분
R, C, map_leather = Input_Data()
 
# 여기서부터 작성
sol = Solve()
 
# 출력하는 부분
print(sol)
