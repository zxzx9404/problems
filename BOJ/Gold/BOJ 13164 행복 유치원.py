# 이미 오름차순으로 정렬된 배열이므로, 각 원소마다의 차이를 구하면 N-1개의 집합이 나옴
# 이 집합들 중 값이 가장 큰 N-K개의 원소를 제거하면 됨

N, K = map(int, input().split())
heights = list(map(int, input().split()))
hei_dif = []
for i in range(N-1):
    hei_dif.append(heights[i+1] - heights[i])

hei_dif.sort(reverse=True)

ans = sum(hei_dif[K-1:])

print(ans)