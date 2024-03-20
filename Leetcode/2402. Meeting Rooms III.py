class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x : x[0])
        rooms = defaultdict(int)
        used = [0]*n
        hq = []

        for s, e in meetings:
            while hq:
                end_t, room = heapq.heappop(hq)
                if end_t <= s:
                    rooms[room] += 1
                    used[room] = 0
                else:
                    heapq.heappush(hq, [end_t, room])
                    break
            if len(hq) < n:
                for i in range(n):
                    if not used[i]:
                        used[i] = 1
                        heapq.heappush(hq, [e, i])
                        break
            
            else:
                end_t, room = heapq.heappop(hq)
                rooms[room] += 1
                delay = end_t - s
                heapq.heappush(hq, [e+delay, room])
        
        while hq:
            end_t, room = heapq.heappop(hq)
            rooms[room] += 1
        
        arr = sorted(list(rooms.items()), key=lambda x : (-x[1], x[0]))

        return arr[0][0]
