class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        sizes = binaryMatrix.dimensions()
        curRow = 0
        curCol = sizes[1] - 1
        leftIndex = -1

        while curRow < sizes[0] and curCol >= 0:
            res = binaryMatrix.get(curRow, curCol)
            if res == 0:
                curRow += 1
            else:
                leftIndex = curCol
                curCol -= 1
        return leftIndex