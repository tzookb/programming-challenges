class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurse(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n in memo:
                return memo[n]

            res = recurse(n-1) + recurse(n-2)
            memo[n] = res
            return res
        return recurse(n)