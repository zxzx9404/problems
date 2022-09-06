n, gojang = int(input()), int(input())

# 고장버튼이 0개라면 바로 맨 밑으로
if gojang:
    # 고장이 2개 이상이면
    if gojang > 1:
        arr = list(map(int, input().split()))
    # 고장이 1개면
    elif gojang == 1:
        arr = [int(input())]
    
    # 투포인터를 위한 인덱스
    i = -1
    p1, p2 = True, True
    while p1 and p2 and i < abs(100-n):
        i += 1
        # 윗 방향으로 탐색
        n1 = n + i
        # 아랫 방향으로 탐색
        n2 = n - i

        # 윗 방향으로 탐색하면서 온전히 누를 수 있는 가장 가까운 채널 찾기
        for t in str(n1):
            if int(t) in arr:
                break
        else:
            p1 = False
        # 아랫 방향으로 탐색하면서 온전히 누를 수 있는 가장 가까운 채널 찾기    
        if n2 >= 0:
            for t in str(n2):
                if int(t) in arr:
                    break
            else:
                p2 = False

    # 둘을 동시에 찾았으면, 자릿수가 다를 수 있으므로 비교해서 낮은 값 출력
    if not p1 and not p2:
        print(min(i + min(len(str(n1)), len(str(n2))), abs(100 - n)))
    elif not p1:
        print(min(i + len(str(n1)), abs(100 - n)))
    else:
        print(min(i + len(str(n2)), abs(100 - n)))
        
# 고장버튼이 0개면 번호를 직접 눌렀을 떄와 +/- 버튼만으로 이동하는것 중 작은수 출력
else:
    print(min(len(str(n)), abs(100-n)))