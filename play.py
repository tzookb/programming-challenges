from typing import Optional

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        sol = []
        dfs = []
        counted = k
        for i in range(9, 0, -1):
            dfs.append(i)
        
        while dfs:
            cur = dfs.pop()
            if cur > n:
                continue


            sol.append(cur)
            counted -= 1
            if counted == 0:
                return cur
            nextLevel = cur * 10
            for i in range(9, -1, -1):
                dfs.append(nextLevel + i)
        
    def isNbiggerThankids(self, n, curNum):
        
        

s = Solution()
res = s.findKthNumber(13, 2)
print(res)
