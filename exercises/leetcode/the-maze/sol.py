from typing import List

class Solution:
    def isPointsEqual(self, p1: List[int], p2: List[int]) -> bool:
        return p1[0] == p2[0] and p1[1] == p2[1]

    def hasPathFrom(self, maze: List[List[int]], cur: List[int], destination: List[int], source: str) -> bool:
        if self.isPointsEqual(cur, destination):
            return True
        

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.hasPathFrom(maze, start, destination, "none")
        print(maze, start, destination)

s = Solution()
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
start = [0, 4]
dest = [4, 4]
res = s.hasPath(maze, start, dest)
print(res)