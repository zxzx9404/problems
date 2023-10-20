from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        if grid[0][0] + grid[N-1][N-1]:
            return -1
        
        di = [-1, -1, -1, 0, 1, 1, 1, 0]
        dj = [-1, 0, 1, 1, 1, 0, -1, -1]
        dq = deque()
        dq.append((0, 0))
        grid[0][0] = 2
        
        while dq:
            i, j = dq.popleft()
            for k in range(8):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and not grid[ni][nj]:
                    grid[ni][nj] = grid[i][j] + 1
                    dq.append((ni, nj))
                    
        return grid[N-1][N-1] - 1 if grid[ni][nj] else -1
