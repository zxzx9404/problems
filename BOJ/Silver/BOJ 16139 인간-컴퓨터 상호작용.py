import sys
input = sys.stdin.readline

word = input().strip()
N = int(input())
ans_list = [[0]*26 for _ in range(len(word))]

for i in range(len(word)):
    for j in range(26):
        ans_list[i][j] = ans_list[i-1][j]
    
    idx = ord(word[i]) - 97
    ans_list[i][idx] += 1

for _ in range(N):
    a, l, r = input().split()
    a = ord(a) - 97
    l = int(l)
    r = int(r)
    
    if not l:
        print(ans_list[r][a])
    else:
        print(ans_list[r][a]-ans_list[l-1][a])
        

'''
import sys
input = sys.stdin.readline

word = input().strip()
N = int(input())

ans_dict = dict()

for i in range(len(word)):
    ans_dict[i] = dict()
    
    for j in range(26):
        if not i:
            ans_dict[i][j] = 0   
        else:
            ans_dict[i][j] = ans_dict[i-1][j]

    idx = ord(word[i]) - 97
    ans_dict[i][idx] += 1

for _ in range(N):
    a, l, r = input().split()
    a = ord(a) - 97
    l = int(l)
    r = int(r)
    
    if not l:
        print(ans_dict[r][a])
    else:
        print(ans_dict[r][a]-ans_dict[l-1][a])
'''