from typing import Counter, List, Optional

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        grid = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        max_val = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    continue
                r = row + 1
                c = col + 1
                new_val = min(
                    grid[r - 1][c],
                    grid[r - 1][c-1],
                    grid[r][c-1],
                ) + 1
                grid[r][c] = new_val
                max_val = max(max_val, new_val)

        return max_val ** 2

matrix = [
    ["0","0","0","1"],
    ["1","1","0","1"],
    ["1","1","1","1"],
    ["0","1","1","1"],
    ["0","1","1","1"]
]

matrix = [
    ["1","1","1"],
    ["1","1","1"],
    ["1","1","1"]
]

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

s = Solution()
res = s.maximalSquare(matrix)
print(res)
