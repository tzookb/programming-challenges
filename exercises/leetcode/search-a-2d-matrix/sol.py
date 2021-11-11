class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = 0
        
        while row >= 0 and col < len(matrix[0]):
            cur = matrix[row][col]
            if cur == target:
                return True
            elif cur > target:
                row -= 1
            else:
                col += 1
        return False
        