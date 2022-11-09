from itertools import permutations, combinations

word = list(input())
N = len(word)

if N == 1:
    print(1)
elif N == 2:
    if word[0] == word[1]:
        print(0)
    else:
        print(2)
else:
    perm = (permutations(word, N))
    ans = set()
    for temp in perm:
        for i in range(1, N-1):
            if temp[i] == temp[i-1] or temp[i] == temp[i+1]:
                break
        else:
            ans.add(temp)

print(len(ans))