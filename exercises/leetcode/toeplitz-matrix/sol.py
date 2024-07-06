class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 or col == 0:
                    continue
                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False
        return True