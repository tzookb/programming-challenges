class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        paths = [[0 for _ in range(cols)] for _ in range(rows)]
        
        prev = 0
        for i in range(cols):
            paths[0][i] = grid[0][i] + prev
            prev = paths[0][i]

        prev = 0
        for i in range(rows):
            paths[i][0] = grid[i][0] + prev
            prev = paths[i][0]

        
        for row in range(1, rows):
            for col in range(1, cols):
                paths[row][col] = min(
                    paths[row - 1][col],
                    paths[row][col - 1]
                ) + grid[row][col]

        return paths[-1][-1]
