# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        n = len(rooms)
        queue = [0]

        while queue:
            room = queue.pop(0)

            if room in visited:
                continue
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
        
        return len(visited) == n
