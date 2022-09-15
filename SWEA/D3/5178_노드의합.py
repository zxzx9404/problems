# 모든 노드의 값을 구하는 정석적인 풀이

TC = int(input())

for tc in range(1, TC+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    for i in range(N, 0, -1):
        if tree[i] == 0:
            tree[i] += tree[i*2]
            if i*2+1 <= N:
                tree[i] += tree[i*2+1]
    print(f'#{tc} {tree[L]}')



# 트리를 만들지 않고 답을 구하는 변칙적인? 풀이

def find_leaf(n):
    global ans
    if n <= N:
        find_leaf(n*2)
        find_leaf(n*2+1)
        if n in arr:
            ans += arr2[arr.index(n)]

TC = int(input())

for tc in range(1, TC+1):
    N, M, L = map(int, input().split())
    ans = 0
    arr, arr2 = [], []
    for _ in range(M):
        a, b = map(int, input().split())
        arr.append(a)
        arr2.append(b)
    find_leaf(L)
    print(f'#{tc} {ans}')