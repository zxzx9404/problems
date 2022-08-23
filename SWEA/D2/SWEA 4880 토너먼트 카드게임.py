# arr에서 토너먼트를 치룬 결과를 arr2에 저장
# arr2에서 다음 토너먼트를 치룬 결과를 다시 arr에 저장
# 최종 승자가 나올때까지 위 과정을 반복

def winner(lst): # arr 토너먼트
    global arr2
    # 원소가 1개
    if len(lst) == 1:
        arr2.append(lst[0])
        return
    # 원소가 2개
    elif len(lst) == 2:
        if (lst[0][0] == 1 and lst[1][0] == 3) or (lst[0][0] == 2 and lst[1][0] == 1) or (lst[0][0] == 3 and lst[1][0] == 2) or lst[0][0] == lst[1][0]:
            del lst[1]
        else:
            del lst[0]
        arr2.append(lst[0])
        return
    # 원소가 2개 이상
    else:
        lst1 = lst[:((len(lst)+1)//2)]
        lst2 = lst[((len(lst)+1)//2):]
        #반씩 잘라서 재귀 호출
        winner(lst1)
        winner(lst2)


def winner2(lst): # arr2 토너먼트
    global arr
    if len(lst) == 1:
        arr.append(lst[0])
        return
    elif len(lst) == 2:
        if (lst[0][0] == 1 and lst[1][0] == 3) or (lst[0][0] == 2 and lst[1][0] == 1) or (lst[0][0] == 3 and lst[1][0] == 2) or lst[0][0] == lst[1][0]:
            del lst[1]
        else:
            del lst[0]
        arr.append(lst[0])
        return
    else:
        lst1 = lst[:((len(lst)+1)//2)]
        lst2 = lst[((len(lst)+1)//2):]
        winner2(lst1)
        winner2(lst2)




TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    original = list(map(int, input().split()))
    arr, arr2 = [], []

    for i in range(n): # 참가자마다 위치 번호를 저장한 이중 배열로 재구성
        arr.append([original[i], i+1])

    while True:
        if arr2 == []:
            winner(arr)
            arr.clear()
            if len(arr2) == 1:
                break
        elif arr == []:
            winner2(arr2)
            arr2.clear()
            if len(arr) == 1:
                break
    if arr:
        print(f'#{tc} {arr[0][1]}')
    else:
        print(f'#{tc} {arr2[0][1]}')

