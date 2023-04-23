from collections import deque

# 소수 판별 함수
def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num == 1 or num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num**0.5)+1, 6):
        if num % i == 0 or num % (i+2) == 0:
            return False
    return True

def bfs(num):
    visited = [0]*1000003
    q = deque([(num, 0)])

    while q:
        num, cnt = q.popleft()

        for new_num in (num//2, num//3, num+1, num-1):
            if not visited[new_num]:
                if new_num in primes:
                    print(cnt+1)
                    return
                elif 0 < new_num <= 1000001:
                    visited[new_num] = True
                    q.append((new_num, cnt+1))

TC = int(input())

for _ in range(TC):
    now, min_t, max_t = map(int, input().split())
    
    primes = []
    for num in range(min_t, max_t+1):
        if is_prime(num):
            primes.append(num)
    
    if not primes:
        print(-1)
        continue
    
    if min_t <= now <= max_t and now in primes:
        print(0)
        continue

    bfs(now)