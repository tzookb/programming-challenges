from typing import List

class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}

        visited_count = 0

        go_through = [0]
        while go_through and visited_count < len(rooms):
            cur = go_through.pop(0)
            if cur in visited:
                continue

            visited[cur] = True
            visited_count += 1
            go_through += rooms[cur]
        
        return visited_count == len(rooms)

rooms = [[1,3],[3,0,1],[2],[0]]
s = Solution()
res = s.canVisitAllRooms(rooms)
print(res)