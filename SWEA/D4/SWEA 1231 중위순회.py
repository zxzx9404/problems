# 중위 순회 함수
def inorder(V):
    if V:
        inorder(ch1[V])
        print(word[V], end='')
        inorder(ch2[V])


for tc in range(1, 11):
    n = int(input())
    # 각 노드에 해당하는 알파벳을 담을 배열
    word = ['']*(n+1)
    ch1 = [0]*(n+1)
    ch2 = [0]*(n+1)
    for _ in range(n):
        arr = input().split()
        # 자식 노드가 2개일 경우
        if len(arr) == 4:
            # ch1, ch2 각각 배정    
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
        # 자식 노드가 1개일 경우
        elif len(arr) == 3:
            ch1[int(arr[0])] = int(arr[2])
        # word 배열에 각 노드에 해당하는 문자 저장
        word[int(arr[0])] = arr[1]
    print(f'#{tc}', end=' ')
    # 중위 순회하며 각 노드에 해당하는 문자 출력
    inorder(1)
    print()