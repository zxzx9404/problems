# 실행시간 : 68ms

def preorder(V):
    if V:
        print(chr(V+64), end='')
        preorder(ch1[V])
        preorder(ch2[V])
        
def inorder(V):
    if V:
        inorder(ch1[V])
        print(chr(V+64), end='')
        inorder(ch2[V])

def postorder(V):
    if V:
        postorder(ch1[V])
        postorder(ch2[V])
        print(chr(V+64), end='')

n = int(input())
ch1 = [0]*(n+1)
ch2 = [0]*(n+1)
for _ in range(n):
    arr = input().split()
    if arr[1] != '.':
        ch1[ord(arr[0])-64] = ord(arr[1]) - 64
    if arr[2] != '.':
        ch2[ord(arr[0])-64] = ord(arr[2]) - 64

preorder(1)
print()
inorder(1)
print()
postorder(1)