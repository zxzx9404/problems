# 트리에 값을 넣는 방식이 중위 순회와 같으므로, 중위순회 방식 채택
def inorder(o):
    global cnt
    if o <= n:
        inorder(o * 2)
        tree[o] = cnt
        cnt += 1
        inorder(o * 2 + 1)


TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    tree = [0]*(n+1)
    cnt = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[n//2]}')
