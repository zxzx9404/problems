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
