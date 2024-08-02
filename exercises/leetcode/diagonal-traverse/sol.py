import itertools

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagnols = []
        for row in range(len(mat)):
            diagnols.append(
                self.getDiagnol(row, 0, mat)
            )
        for col in range(1, len(mat[0])):
            diagnols.append(
                self.getDiagnol(len(mat) - 1, col, mat)
            )
        
        for i in range(len(diagnols)):
            if i % 2:
                diagnols[i] = diagnols[i][::-1]
        

        return list(itertools.chain.from_iterable(diagnols))
        

    def getDiagnol(self, row: int, col: int, mat: List[List[int]]) -> List[int]:
        diagnol = []
        while row >= 0 and col < len(mat[0]):
            diagnol.append(mat[row][col])
            row -= 1
            col += 1
        
        return diagnol

        