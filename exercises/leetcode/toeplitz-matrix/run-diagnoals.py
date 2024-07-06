class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for row in range(len(matrix)):
            if not self.checkDiagnol(matrix, [row, 0]):
                return False
        
        for col in range(len(matrix[0])):
            if not self.checkDiagnol(matrix, [0, col]):
                return False
        
        return True
    
    def checkDiagnol(self, matrix: List[List[int]], start: List[int]) -> bool:
        row = start[0]
        col = start[1]
        val = matrix[row][col]

        while row < len(matrix) and col < len(matrix[0]):
            cur = matrix[row][col]
            if cur != val:
                return False
            row += 1
            col += 1
        
        return True
        