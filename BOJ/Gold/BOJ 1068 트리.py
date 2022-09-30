## 문제풀이 아이디어
'''
받은 리스트가 그대로 부모 노드를 의미
제거할 노드의 부모 노드를 임의의 숫자(-2)로 만듬
재귀문을 통해, 제거된 노드를 추종하던 자식 노드들도 모두 -2로 만듬

위 과정이 끝난 후에, 리스트를 순회하면서 -2가 아니고, 자신을 따르는 노드가 없는
노드들을 찾으면 됨
'''

def dfs(c):
    while c in par:
        dfs(par.index(c))
        par[par.index(c)] = -2

N = int(input())
par = list(map(int, input().split()))
c = int(input())

par[c] = -2
dfs(c)

cnt = 0
for i in range(N):
    if i not in par and par[i] != -2:
        cnt += 1
        
print(cnt)