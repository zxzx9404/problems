T = int(input())

for i in range(T):
    n = int(input())
    weardict = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    cnt = 1

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)


# dict의 value가 list 형태라면, append가 가능하다