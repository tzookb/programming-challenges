from typing import List
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows_sums = self.getRowsSumMatrix(mat)
        sol = self.getZeroedMat(mat)

        def getTotalFrom(row, c_left, c_right):
            if row < 0 or row >= len(rows_sums):
                return 0

            sum_arr = rows_sums[row]

            if c_right >= len(sum_arr):
                c_right = len(sum_arr) - 1
            if c_left <= 0:
                return sum_arr[c_right]
            return sum_arr[c_right] - sum_arr[c_left - 1]

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                left = c - k
                right = c + k
                total = 0
                for row in range(r - k, r + k + 1):
                    cur_row_sum = getTotalFrom(row, left, right)
                    total += cur_row_sum
                
                sol[r][c] = total

        return sol

    def getZeroedMat(self, mat: List[List[int]]) -> List[List[int]]:
        return [[0 for col in range(len(mat[0]))] for row in range(len(mat))]

    def getRowsSumMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = self.getZeroedMat(mat)

        for r in range(len(mat)):
            prev = 0
            for c in range(len(mat[0])):
                cur = prev + mat[r][c]
                res[r][c] = cur
                prev = cur
        return res

    def getTopSumMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = self.getZeroedMat(mat)
        def getSumFromPoint(r, c):
            if r < 0 or r >= len(mat):
                return 0
            if c < 0 or c >= len(mat[0]):
                return 0
            return res[r][c]
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                total = (
                    getSumFromPoint(r - 1, c)
                    + getSumFromPoint(r, c - 1) 
                    - getSumFromPoint(r - 1, c - 1)
                    + mat[r][c]
                )
                res[r][c] = total
        return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
s = Solution()
res = s.matrixBlockSum(matrix, k)
print(res)