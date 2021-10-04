from typing import List

class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def recu(size):
            if size <= 1:
                return 1
            if size in memo:
                return memo[size]
            total = 0
            for i in range(1, size + 1):
                total += (
                    recu(i - 1) *
                    recu(size - i)
                )
            memo[size] = total
            return total
        return recu(n)

s = Solution()
res = s.numTrees(3)
print(res)
