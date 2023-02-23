def solution(n, m, x, y, r, c, k):
    if abs(x-r) + (y-c) > k or abs(x-r) + (y-c) - k % 2 == 1:
        return 'impossible'

    answer = ''
    
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    alpha = ['d', 'l', 'r', 'u']

    q = [(x, y, k)]

    while q:
        i, j, left = q.pop(0)
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < n and 0 <= nj < m and left:
                q.append((ni, nj, left-1))
                answer += alpha[k]

    return answer


print(solution(3, 3, 1, 2, 3, 3, 4))