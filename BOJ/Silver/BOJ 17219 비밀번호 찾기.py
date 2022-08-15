import sys
input = sys.stdin.readline


N, M = map(int, input().split())

dict = dict()
for _ in range(N):
    a, b = input().split()
    dict[a] = b

for i in range(M):
    c = input().rstrip()
    print(dict[c])