import sys
sys.setrecursionlimit(100000000)

### 로직의 작동 방식 ###
'''
ans에 0을 넣고 재귀 -> 또 0이 들어가고 재귀 -> m번 반복
m번 반복하면 ans의 원소들의 인덱스에 해당하는 arr 출력

4번 기준으로

0000
0001
0002
0003 순으로 들어가게 됨
'''


def back(st, ans):
    if len(ans) == m:
        for i in ans:
            print(arr[i], end=' ')
        print()
        return

    for j in range(st, len(arr)):
        back(j, ans+[j])

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))


for o in range(len(arr)):
    back(o, [o])