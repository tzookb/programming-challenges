from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        steps = matrix[0][:]

        for row in range(1, len(matrix)):
            next_steps = []
            for col in range(len(matrix[row])):
                options = []
                if col > 0:
                    options.append(steps[col - 1])
                if col < len(matrix[row]) - 1:
                    options.append(steps[col + 1])
                options.append(steps[col])

                next_steps.append(
                    matrix[row][col] + min(options)
                )
            steps = next_steps
        
        return min(steps)



        
# [1,2,3,4,5]
# [5,1,2,3,5]
# [9,1,1,2,3]

s = Solution()
mat = [[-19,57],[-40,-5]]
res = s.minFallingPathSum(mat)
print(res)
