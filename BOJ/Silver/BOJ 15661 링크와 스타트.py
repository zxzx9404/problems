def cal_cha(team):
    team_hap = 0
    
    for i in team:
        for j in team:
                team_hap += arr[i][j]

    return team_hap
    

def dfs(s, cnt, n):
    global ans
    
    if cnt == n:
        start, link = [], []
        
        for i in range(N):
            if visited[i]:
                start.append(i)
            else:
                link.append(i)
    
        if not len(start) or not len(link):
            return 
        
        team_cha = abs(cal_cha(start) - cal_cha(link))
        ans = min(ans, team_cha)
        return
    
    for i in range(s, N):
        if not visited[i]:
            visited[i] = True
            dfs(s+1, cnt+1, n)
            visited[i] = False

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
ans = N * 100

for i in range(1, N//2+1):
    dfs(0, 0, i)

print(ans)