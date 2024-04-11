# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        nrooms = len(rooms)
        visited = set()
        visited.add(0)

        q = deque()
        q.append(0)

        while q:
            curr_room = q.popleft()
            for key in rooms[curr_room]:
                if key not in visited:
                    q.append(key)
                    visited.add(key)

        return len(visited) == nrooms
                    
            