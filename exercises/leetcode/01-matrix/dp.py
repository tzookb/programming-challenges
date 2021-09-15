from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        length = len(mat)
        width = len(mat[0])

        sol = self.getMaxMat(length, width)

        # from top left to bottom right
        for r in range(length):
            for c in range(width):
                val = mat[r][c]
                if val == 0:
                    sol[r][c] = 0
                    continue

                options = [sol[r][c]]
                if r > 0:
                    options.append(sol[r - 1][c] + 1)
                if c > 0:
                    options.append(sol[r][c - 1] + 1)
                
                sol[r][c] = min(options)

        # from bottom right to top left
        for r in range(length - 1, -1, -1):
            for c in range(width - 1, -1, -1):
                val = mat[r][c]
                if val == 0:
                    sol[r][c] = 0
                    continue

                options = [sol[r][c]]
                if r < length - 1:
                    options.append(sol[r + 1][c] + 1)
                if c < width - 1:
                    options.append(sol[r][c + 1] + 1)
                
                sol[r][c] = min(options)

        return sol

    def getMaxMat(self, length, width) -> List[List[int]]:
        maxVal = float("inf")
        return [[maxVal for col in range(width)] for row in range(length)]

s = Solution()
# mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
res = s.updateMatrix(mat)
print(res)