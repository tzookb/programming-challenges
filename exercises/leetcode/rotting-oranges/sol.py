from typing import List

EMPTY = 0
FRESH = 1
ROTTEN = 2
class Solution:
    
    def is_near_rotten(self, x, y, grid: List[List[int]]) -> bool:
        height = len(grid)
        width = len(grid[0])
        if y > 0:
            if grid[y-1][x] == ROTTEN:
                return True
        if y < height - 1:
            if grid[y+1][x] == ROTTEN:
                return True
        if x > 0:
            if grid[y][x-1] == ROTTEN:
                return True
        if x < width - 1:
            if grid[y][x+1] == ROTTEN:
                return True
        return False

    def print(self, grid: List[List[int]]):
        for row in grid:
            print(row)
        print("-----")

    def orangesRotting(self, grid: List[List[int]]) -> int:
        updates = []
        rounds = 0
        while True:
            for y, row in enumerate(grid):
                for x, _ in enumerate(row):
                    if grid[y][x] == ROTTEN or grid[y][x] == EMPTY:
                        continue
                    if self.is_near_rotten(x, y, grid):
                        updates.append((x, y))
            self.print(grid)
            if not updates:
                break
            rounds += 1
            for update in updates:
                grid[update[1]][update[0]] = ROTTEN
            updates = []

        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                if grid[y][x] == FRESH:
                    return -1
        
        return rounds