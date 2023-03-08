from heapq import heappush, heappop, heapify

def solution(genres, plays):
    answer = []
    dct = dict()
    for idx, genre, play in zip(range(len(genres)), genres, plays):
        if dct.get(genre):
            dct[genre][0] -= play
            heappush(dct[genre][1], (-play, idx))
        else:
            dct[genre] = [-play, [(-play, idx)]]
    
    arr = sorted(dct.values())
    heapify(arr)
    
    while arr:
        acc, songs = heappop(arr)
        for i in range(2):
            if songs:
                answer.append(heappop(songs)[1])
    
    return answer