class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])
        dp = [[0] * (width + 1) for _ in range(height + 1)]
        ans = 0
        
        for r in range(height):
            for c in range(width):
                if matrix[r][c] == 0:
                    continue
                cur = min(
                    dp[r][c],
                    dp[r + 1][c],
                    dp[r][c + 1]
                ) +  1

                dp[r+1][c+1] = cur
                ans += cur
        
        return ans
