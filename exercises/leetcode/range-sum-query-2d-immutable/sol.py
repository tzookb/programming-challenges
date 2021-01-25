from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.calcPrepSum(matrix)

    def calcPrepSum(self, matrix: List[List[int]]):
        self.sums = []
        for row in matrix:
            temp_sums = [0]
            for val in row:
                temp_sums.append(temp_sums[-1] + val)
            temp_sums.pop(0)
            self.sums.append(temp_sums)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0        
        for curRow in range(row1, row2+1):
            startSum = 0 if col1 == 0 else self.sums[curRow][col1-1]
            endSum = self.sums[curRow][col2]
            total += endSum - startSum
        return total



matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

s = NumMatrix(matrix)
print(s.sumRegion(2, 1, 4, 3)) # 8
print(s.sumRegion(1, 1, 2, 2)) # 11
print(s.sumRegion(1, 2, 2, 4)) # 12