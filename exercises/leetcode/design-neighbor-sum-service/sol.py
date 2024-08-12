class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        

    def getCellVal(self, row: int, col: int) -> int:
        if row < 0 or row >= len(self.grid):
            return 0
        if col < 0 or col >= len(self.grid[0]):
            return 0
        return self.grid[row][col]

    def adjacentSum(self, value: int) -> int:
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] != value:
                    continue
                return (
                    self.getCellVal(row - 1, col) +
                    self.getCellVal(row + 1, col) +
                    self.getCellVal(row, col - 1) +
                    self.getCellVal(row, col + 1)
                )

    def diagonalSum(self, value: int) -> int:
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] != value:
                    continue
                return (
                    self.getCellVal(row - 1, col - 1) +
                    self.getCellVal(row + 1, col + 1) +
                    self.getCellVal(row - 1, col + 1) +
                    self.getCellVal(row + 1, col - 1)
                )



# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)