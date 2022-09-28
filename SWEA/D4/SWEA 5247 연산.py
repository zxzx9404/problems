from collections import deque
 
def bfs(N, M):
    queue = deque()
    queue.append((N, 0))
    visited = [0] * 1000001
    
    while queue:
        i, count = queue.popleft()
        if visited[i]:
            continue
        
        visited[i] = 1
        
        if i == M:
            return count
        
        count += 1
        
        if 0 < i+1 <= 1000000:
            queue.append((i+1, count))
        if 0 < i-1 <= 1000000:
            queue.append((i-1, count))
        if 0 < i*2 <= 1000000:
            queue.append((i*2, count))
        if 0 < i-10 <= 1000000:
            queue.append((i-10, count))

TC = int(input())
 
for tc in range(1, TC+1):
    N,M = map(int, input().split())
    print(f'#{tc} {bfs(N, M)}')