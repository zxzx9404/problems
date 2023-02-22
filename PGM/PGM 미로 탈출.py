def solution(maps):
    N, M = len(maps), len(maps[0])
    
    def dfs(y, x, param):
        visited = [[0]*M for _ in range(N)]
        q = [(y, x)]
        while q:
            i, j = q.pop(0)
            for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and maps[ni][nj] != 'X':
                    visited[ni][nj] = visited[i][j] + 1
                    if maps[ni][nj] == param:
                        dct = dict()
                        dct['i'] = ni
                        dct['j'] = nj
                        dct['moves'] = visited[ni][nj]
                        return dct
                    q.append((ni, nj))
                    
        return False


    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start_i, start_j = i, j
                break
            
    
    find_lever = dfs(start_i, start_j, 'L')
    
    print(find_lever)
    print(find_lever['i'])
    if find_lever:
        ans = dfs(find_lever['i'], find_lever['j'], 'E')
        if ans:
            return find_lever['moves'] + ans['moves']
        
            
    return -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))