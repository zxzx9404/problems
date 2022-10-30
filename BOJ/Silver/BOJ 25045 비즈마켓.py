N, M = map(int, input().split())

goods = sorted(list(map(int, input().split())), reverse=True)
client = sorted(list(map(int, input().split())))

ans, idx = 0, 0

while idx < N and idx < M:
    if goods[idx] <= client[idx]:
        break
    
    ans += goods[idx] - client[idx]
    idx += 1

print(ans)