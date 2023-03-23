from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    dct = defaultdict(dict)

    for order in orders:
        for num in course:
            arr = combinations(order, num)
            for menu in arr:
                menu = tuple(sorted(menu))
                dct[num][menu] = dct[num].get(menu, 0) + 1

    for num in course:
        arr_sort = sorted(dct[num].items(), key = lambda x : (-x[1], x[0]))
        if arr_sort:
            top = arr_sort[0][1]
            if top > 1:
                answer.append(arr_sort[0][0])

                if len(arr_sort) > 1:
                    for item, value in arr_sort[1:]:
                        if value < top:
                            break
                        answer.append(item)

    return [''.join(item) for item in sorted(answer)]


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5])
solution(["XYZ", "XWY", "WXA"], [2,3,4])