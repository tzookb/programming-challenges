
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for col in range(len(mat[0])):
            diagonal = self.getDiagonal(0, col, mat)
            diagonal.sort()
            self.updateDiagonal(0, col, diagonal, mat)
        
        for row in range(len(mat)):
            diagonal = self.getDiagonal(row, 0, mat)
            diagonal.sort()
            self.updateDiagonal(row, 0, diagonal, mat)

        return mat

    def updateDiagonal(self, row, col, diagnol, mat: List[List[int]]) -> List[int]:
        items = []
        rows_len = len(mat)
        cols_len = len(mat[0])

        for item in diagnol:
            mat[row][col] = item

            row += 1
            col += 1

    def getDiagonal(self, row, col, mat: List[List[int]]) -> List[int]:
        items = []
        rows_len = len(mat)
        cols_len = len(mat[0])

        while True:
            if row > rows_len - 1:
                break
            if col > cols_len - 1:
                break
            cur = mat[row][col]
            items.append(cur)

            row += 1
            col += 1

        return items
