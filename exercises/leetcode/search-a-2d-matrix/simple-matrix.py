class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_size = len(matrix)
        cols_size = len(matrix[0])
        left = 0
        right = rows_size * cols_size - 1

        while left <= right:
            mid = left + (right - left) // 2
            row, col = self.getMatrixIndeces(rows_size, cols_size, mid)
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True

        return False

    def getMatrixIndeces(self, rows: int, columns: int, idx: int):
        row = idx // columns
        col = idx - (row * columns)

        return [row, col]