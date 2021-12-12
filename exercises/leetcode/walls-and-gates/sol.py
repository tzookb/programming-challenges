from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        spots = []
        # find all the gates
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                cur = rooms[row][col]
                if cur == 0:
                    spots.append((row, col, 0))
        

        visited = {}
        while spots:
            [row, col, dist] = spots.pop(0)
            if row < 0 or row >= len(rooms):
                continue
            if col < 0 or col >= len(rooms[0]):
                continue

            key = f"{row}_{col}"
            if key in visited:
                continue
            visited[key] = True

            cur = rooms[row][col]
            if cur == -1:
                continue

            rooms[row][col] = dist
            spots.append((row + 1, col, dist + 1))
            spots.append((row - 1, col, dist + 1))
            spots.append((row, col + 1, dist + 1))
            spots.append((row, col - 1, dist + 1))

arr = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]]
s = Solution()
s.wallsAndGates(arr)
print(arr)
