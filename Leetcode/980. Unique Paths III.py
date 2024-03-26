class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dy = [0, 0, -1, 1]
        dx = [1, -1, 0, 0]

        self.ans = 0
        N = len(grid)
        M = len(grid[0])
        total = 1
        def dfs(y, x, cnt):
            if grid[y][x] == 2:
                self.ans += (cnt == total)
                return

            grid[y][x] = -1
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if 0 > ny or ny == N or 0 > nx or nx == M: continue
                if grid[ny][nx] == -1: continue
                dfs(ny, nx, cnt+1)
            grid[y][x] = 0

        for i in range(N):
            for j in range(M):
                if not grid[i][j]:
                    total += 1
                elif grid[i][j] == 1:
                    sti, stj = i, j
                    grid[i][j] = -1
        
        dfs(sti, stj, 0)

        return self.ans
