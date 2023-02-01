def solution(k, tangerine):
    answer = 0

    dct = dict()

    for i in tangerine:
        dct[i] = dct.get(i, 0) + 1
    
    lst = sorted(list(dct.items()), key=lambda x : x[1], reverse=True)

    for d, n in lst:
        k -= n
        answer += 1
        if k <= 0:
            break
        
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))