import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = set()
look = set()

for _ in range(N):
    listen.add(input().rstrip())

for _ in range(M):
    look.add(input().rstrip())


jap = sorted(list(listen & look))
print(len(jap))
for i in jap:
    print(i)
    

# set을 사용하여 합집합으로 계산
# 출력은 알파벳 순이어야 하니, 합집합을 만든 후 다시 list화 해서 sort