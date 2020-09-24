from typing import List
from collections import Counter

class Solution:
    def getFormulas(self, digits: List[int], formula: str, curVal: int, target: int) -> List[str]:
        if not digits:
            if target == 0:
                return [formula]
            return []
        

    def addOperators(self, num: str, target: int) -> List[str]:
        digits = [int(x) for x in num]
        return self.getFormulas(digits, '', 0, target)

s = Solution()
res = s.addOperators("232", 8) 
print(res)