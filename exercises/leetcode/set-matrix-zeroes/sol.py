import imp
from typing import List

class Solution:
    
    def setZeroesCol(self, matrix: List[List[int]], col: int) -> None:
        for row in range(len(matrix)):
            matrix[row][col] = 0
    
    def setZeroesRow(self, matrix: List[List[int]], row: int) -> None:
        for col in range(len(matrix[0])):
            matrix[row][col] = 0
        
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        for col in cols:
            self.setZeroesCol(matrix, col)
        for row in rows:
            self.setZeroesRow(matrix, row)
