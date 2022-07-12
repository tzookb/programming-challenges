from typing import List

class Solution:
    def getMaxFromGrid(self, grid: List[List[int]]) -> int:
        return max([max(row) for row in grid]);

    def largestIsland(self, grid: List[List[int]]) -> int:
        found_islands = self.getIsalnds(grid)
        grid = self.updateGridIslandsWithSize(grid, found_islands)
        update_mapper = self.getMatrix(len(grid[0]), len(grid))

        
        def keyFromRowCol(row, col):
            return f"{row}_{col}"
        
        def rowColFromKey(key):
            return [int(x) for x in key.split("_")]
        
        for island in found_islands:
            to_update = {}
            size = len(island)
            for pos in island:
                to_update[keyFromRowCol(pos[0]+1, pos[1])] = size
                to_update[keyFromRowCol(pos[0]-1, pos[1])] = size
                to_update[keyFromRowCol(pos[0], pos[1]+1)] = size
                to_update[keyFromRowCol(pos[0], pos[1]-1)] = size

            for pos in to_update:
                row, col = rowColFromKey(pos)
                size_to_bump = to_update[pos]
                if row < 0 or row >= len(grid):
                    continue
                if col < 0 or col >= len(grid[0]):
                    continue
                if grid[row][col] > 0:
                    continue
                update_mapper[row][col] += size_to_bump
            
        max_from_connected = self.getMaxFromGrid(update_mapper) + 1
        max_from_grid = self.getMaxFromGrid(grid)
        return max(max_from_connected, max_from_grid)

    def updateGridIslandsWithSize(self, grid: List[List[int]], found_islands):
        for island in found_islands:
            size = len(island)
            for pos in island:
                grid[pos[0]][pos[1]] = size

        return grid

    def getMatrix(self, width, height):
        return [[0 for x in range(width)] for y in range(height)]

    def getIsalnds(self, grid: List[List[int]]) -> int:
        visited = self.getMatrix(len(grid[0]), len(grid))

        found_islands = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dfs = [(row, col)]
                island = []
                while dfs:
                    cord = dfs.pop()
                    if cord[0] < 0 or cord[0] >= len(grid):
                        continue
                    if cord[1] < 0 or cord[1] >= len(grid[0]):
                        continue
                    if visited[cord[0]][cord[1]]:
                        continue
                    if grid[cord[0]][cord[1]] == 0:
                        continue
                    visited[cord[0]][cord[1]] = True
                    island.append(cord)
                    dfs.append((cord[0]-1, cord[1]))
                    dfs.append((cord[0]+1, cord[1]))
                    dfs.append((cord[0], cord[1]-1))
                    dfs.append((cord[0], cord[1]+1))
                
                if island:
                    found_islands.append(island)

        return found_islands

grid = [
    [1,1,1,0],
    [1,0,0,0],
    [1,0,1,1],
    [1,0,1,1]
]
s = Solution()
res = s.largestIsland(grid)
print(res)