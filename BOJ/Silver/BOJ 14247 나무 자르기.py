# 최초 나무 길이는 어차피 다 가져갈 것.
# 고로 성장치가 낮은 나무부터 캐면 됨

N = int(input())
now = list(map(int, input().split()))
grow = list(map(int, input().split()))

grow.sort()

ans = sum(now)

for i in range(N):
    ans += grow[i] * i

print(ans)