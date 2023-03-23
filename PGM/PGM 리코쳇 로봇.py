from collections import deque

def solution(board):
    N = len(board)
    M = len(board[0])
                    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                visited = [[10**10]*M for _ in range(N)]
                q = deque([(i, j)])
                dy = [0, 0, -1, 1]
                dx = [-1, 1, 0, 0]
                visited[i][j] = 0

                while q:
                    true_y, true_x = q.popleft()

                    for i in range(4):
                        cnt = 0
                        y, x = true_y, true_x
                        while True:
                            ny = y + dy[i]
                            nx = x + dx[i]
                            if 0 > ny or ny == N or 0 > nx or nx == M or board[ny][nx] == 'D':
                                if board[y][x] == 'G':
                                    return visited[true_y][true_x] + 1
                                if cnt > 0 and visited[true_y][true_x] + 1 < visited[y][x] : 
                                    q.append((y, x))
                                    visited[y][x] = visited[true_y][true_x] + 1
                                break
                            y, x = ny, nx
                            cnt += 1
    return -1