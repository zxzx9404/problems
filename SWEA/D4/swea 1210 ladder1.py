import sys

sys.stdin = open('input.txt','r')


def reverse(list):                                         # 사다리를 뒤집어서 탐색을 시작함
    for i in range(50):
        list[i], list[99-i] = list[99-i], list[i]


for tc in range(10):
    n = int(input())
    ladder = []
    for m in range(100):
        ladder.append(list(map(int, input().split())))     # 사다리를 2차원 배열로 입력
        ladder[m].insert(0, 0)                             # 인덱스 에러를 방지하기 위해
        ladder[m].append(0)                                # 사다리의 좌, 우측에도 한줄을 추가
    reverse(ladder)
    ladder.append([0]*102)                                 # 같은 이유로 아래에도 한줄 추가
    for i in range(102):
        if ladder[0][i] == 2:                              # 시작점('2') 찾기
            idx = i
    a, b = 0, idx
    dir = 2                                                # 1 : 우, 2 : 하, 3 : 좌
    
    while a<99:                                            # a 좌표가 맨 하단에 도달할때까지
        if dir == 2 and ladder[a][b-1] == 1:
            dir = 3
        elif dir == 2 and ladder[a][b+1] == 1:
            dir = 1
        elif ladder[a+1][b] == 1:
            dir = 2
        
        if dir == 1:
            b += 1
        elif dir == 2:
            a += 1
        elif dir == 3:
            b -= 1
        

    print(f'#{n} {b-1}')                                   # 좌측에 임의의 한줄을 추가했으니 -1로 출력