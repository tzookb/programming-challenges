from typing import List, Optional


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        if len(grid) == 1:
            return Node(
                grid[0][0],
                True,
                None,
                None,
                None,
                None,
            )

        top_left = self.construct(self.getSquare(grid, "topleft"))
        top_right = self.construct(self.getSquare(grid, "topright"))
        bottom_left = self.construct(self.getSquare(grid, "bottomleft"))
        bottom_right = self.construct(self.getSquare(grid, "bottomright"))
        
        return Node(
            1,
            False,
            top_left,
            top_right,
            bottom_left,
            bottom_right
        )
    
    def getSquare(self, grid: List[List[int]], pos: str) -> List[List[int]]:
        half_size = len(grid) // 2
        rows = grid[0:half_size] if pos in ["topleft", "topright"] else grid[half_size:]

        res = []
        for row in rows:
            colls = row[0:half_size] if pos in ["topleft", "bottomleft"] else row[half_size:]
            # print("collscollscolls", row, colls, half_size, pos)
            res.append(colls)
        
        return res

grid = [[0,1],[1,0]]
s = Solution()
res = s.construct(grid)
print(res)