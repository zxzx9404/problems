from itertools import combinations
import sys
readl = sys.stdin.readline

def dfs(depth):
    if depth == 15:
        return 1
    
    t1, t2 = games[depth]
    for x, y in ((0,2), (1,1), (2,0)):
        if result[t1][x] > 0 and result[t2][y] > 0:
            result[t1][x] -= 1
            result[t2][y] -= 1
            if dfs(depth+1): return 1
            result[t1][x] += 1
            result[t2][y] += 1
    return 0

def Input_Data():
	n = map(int, readl().split())
	result = [[next(n) for w in range(3)] for t in range(6)]
	return result

games = list(combinations(range(6), 2))
sol_list = []
for _ in range(4):
    result = Input_Data()
    for team in result:
        if sum(team) != 5:
            sol_list.append(0)
            break
    else:
        cnt = dfs(0)
        sol_list.append(cnt)
    
print(*sol_list)
