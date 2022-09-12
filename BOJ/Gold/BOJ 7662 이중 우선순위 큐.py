# 실행 시간 - PyPy : 3608ms / Python : 7756ms
# 음.. 굳이 알아야 하는 개념인가? 싶지만 언젠가 쓸 수도 있으니 알아두자

import heapq
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    # 최소 힙, 최대 힙 두개를 만듬
    q1, q2 = [], []
    # 한 쪽에서 삭제되면, 다른 쪽에서도 삭제하기 위한 visited list
    visited = [False] * k

    for j in range(k):
        com, num = input().split()
        # push의 경우 양쪽에 모두 추가
        if com == 'I':
            heapq.heappush(q1, (int(num), j))
            heapq.heappush(q2, (-int(num), j))
            # 삭제되지 않은 원소의 경우 visited를 True로
            visited[j] = True

        else:
            if num == '1':
                # visited를 확인하여, 일단 삭제된 원소를 쳐냄
                while q2 and not visited[q2[0][1]]:
                    heapq.heappop(q2)

                if q2:
                    visited[q2[0][1]] = False
                    heapq.heappop(q2)
            else:
                # visited를 확인하여, 일단 삭제된 원소를 쳐냄
                while q1 and not visited[q1[0][1]]:
                    heapq.heappop(q1)
                    
                if q1:
                    visited[q1[0][1]] = False
                    heapq.heappop(q1)

    # 최종적으로도 visited를 통하여 삭제된 원소를 쳐냄
    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)


    if not q1 or not q2:
        print("EMPTY")
    else:
        a = -q2[0][0]
        b = q1[0][0]
        print(f'{a} {b}')