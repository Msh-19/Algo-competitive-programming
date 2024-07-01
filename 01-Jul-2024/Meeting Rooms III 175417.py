# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused = [i for i in range(n)]
        ongoing = []
        used = [0] * n
        meetings.sort()

        for start, end in meetings:
            while ongoing and start >= ongoing[0][0]:
                time, room = heappop(ongoing)
                heappush(unused, room)
            
            if unused:
                room = heappop(unused)
                heappush(ongoing, (end, room))
                used[room] += 1
            else:
                time, room = heappop(ongoing)
                heappush(ongoing, (end - start + time, room))
                used[room] += 1
        
        return used.index(max(used))
            