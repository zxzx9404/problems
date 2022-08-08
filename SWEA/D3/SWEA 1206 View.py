import sys

sys.stdin = open('input.txt','r')

tc = 10 #총 테스트 케이스가 input data로 주어지지 않아서 수기 입력

for i in range(1, tc+1):
    n = int(input())
    ans = 0
    list_tc = list(map(int, input().split())) # 층수를 리스트로 저장
    for j in range(2, n-1):
        list_b = []
        temp_min = 255
        if list_tc[j] > list_tc[j-1] and list_tc[j] > list_tc[j-2] and list_tc[j] > list_tc[j+1] and list_tc[j] > list_tc[j+2]:
            list_b.append(list_tc[j] - list_tc[j-1])
            list_b.append(list_tc[j] - list_tc[j-2])
            list_b.append(list_tc[j] - list_tc[j+1])
            list_b.append(list_tc[j] - list_tc[j+2])
            for k in list_b:
                if temp_min >= k:
                    temp_min = k
            ans += temp_min
    print(f'#{i} {ans}')

'''
j번째 건물에 있어서 조망권이 확보된 세대 수는, 본인을 기준으로 앞 2개의 건물의 층수와의 차이
뒷 2개의 건물들과의 층수 차이 중 가장 작은 값이다.

우선 j번째 건물이 앞2 뒤2번째 건물들보다 높은지 확인한 후, 해당 높이 차 중 가장 낮은 값을 세대수로 저장하여 누적합을 계산
'''