dz = (1, -1, 0, 0, 0, 0)
dy = (0, 0, 1, -1, 0, 0)
dx = (0, 0, 0, 0, 1, -1)


def main():
    def find_place(word):
        for i in range(L):
            for j in range(R):
                for k in range(C):
                    if arr[i][j][k] == word:
                        visited[i][j][k] = 0
                        return (i, j, k)
    
    while True: 
        L, R, C = map(int, input().split())
        if not (L+R+C):
            break
        arr = []
        for i in range(L):
            temp = [input() for _ in range(R)]
            input()
            arr.append(temp)

        visited = [[[10**8]*C for _ in range(R)] for _ in range(L)]
        flag = True      

        start = find_place('S')

        q = [start]

        while q:
            z, y, x = q.pop(0)
            for i in range(6):
                nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
                if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C and arr[nz][ny][nx] != '#' and visited[nz][ny][nx] > visited[z][y][x] + 1:
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    q.append((nz, ny, nx))
                    if arr[nz][ny][nx] == 'E':
                        print(f'Escaped in {visited[nz][ny][nx]} minute(s).')
                        q = []
                        flag = False
                        break

        if flag:
            print('Trapped!')
            

if __name__ == '__main__':
    main()