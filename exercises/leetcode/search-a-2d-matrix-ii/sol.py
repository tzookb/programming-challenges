from typing import List
class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix) - 1
        col = 0

        def isOut(row, col):
            return (
                row < 0 or row >= len(matrix) or
                col < 0 or col >= len(matrix[0])
            )

        while True:
            if isOut(row, col):
                return False
            cur = matrix[row][col]
            if cur > target:
                row -= 1
            elif cur < target:
                col += 1
            else:
                return True

s = Solution()
mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
res = s.searchMatrix(mat, 1222)
print(res)