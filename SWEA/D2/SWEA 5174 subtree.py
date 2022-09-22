# 서브트리 개수 세는 함수
def count_subtree(n):
    global cnt
    if n:
        cnt += 1
        count_subtree(ch1[n])
        count_subtree(ch2[n])
        
        
TC = int(input())

for tc in range(1, TC+1):
    E, N = map(int, input().split())
    V = E + 1
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    cnt = 0
    arr = list(map(int, input().split()))
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if not ch1[p]:
            ch1[p] = c
        else:
            ch2[p] = c
    count_subtree(N)
    print(f'#{tc} {cnt}')
    