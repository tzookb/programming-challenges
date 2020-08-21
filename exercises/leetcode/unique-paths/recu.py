class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(x, y, m, n):
            combKey = f"{x}_{y}_{m}_{n}"
            if combKey in memo:
                return memo[combKey]

            if x >= m or y >= n:
                memo[combKey] = 0
                return 0
            if x + 1 == m and y + 1 == n:
                memo[combKey] = 1
                return 1
            
            res = (
                dfs(x + 1, y, m, n) +
                dfs(x, y + 1, m, n)
            )
            memo[combKey] = res
            return res
        
        res = dfs(0, 0, m, n)
        return res