n, k = map(int, input().split())

ondos = list(map(int, input().split()))

ondo_hap = []
ondo_hap.append(sum(ondos[:k])) 

for i in range(n-k):
    ondo_hap.append(ondo_hap[i] - ondos[i] + ondos[k+i])

print(max(ondo_hap))
