# 순열 구하는 함수
def perm(A, n, s, r):
    if s == r:
        arr2.append(p[:])
        return
    for i in range(n):
        if used[i] == 0:
            used[i] = 1
            p[r] = A[i]
            perm(A, n, s, r+1)
            used[i] = 0

# 3개의 숫자가 run or triplet인지 확인하는 함수
def babygin(B):
    for A in B:
        if A[0] == A[1] == A[2] or A[0]+2 == A[1]+1 == A[2]:
            return True
    return False

TC = int(input())

for tc in range(1, TC+1):
    arr = list(map(int, input().split()))
    # 각 플레이어가 받은 카드
    p1, p2 = [], []
    # 3장부터 판별이 필요하므로, 2장까진 그냥 배부
    for i in range(2):
        p1.append(arr[i*2])
        p2.append(arr[i*2+1])

    # 3장째부터 카드를 받을때마다 순열을 생성하여 babygin 여부를 판단
    for i in range(2, 6):
        p1.append(arr[i*2])
        arr2 = []
        p = [0] * 3
        used = [0]*(i+1)
        perm(p1, i+1, 3, 0)
        t = babygin(arr2)
        if t:
            print(f'#{tc} 1')
            break

        p2.append(arr[i*2+1])
        arr2 = []
        p = [0] * 3
        used = [0]*(i+1)
        perm(p2, i+1, 3, 0)
        t = babygin(arr2)
        if t: 
            print(f'#{tc} 2')
            break
        
    # 아무도 babygin 달성하지 못했을 시 0 출력
    else:
        print(f'#{tc} 0')