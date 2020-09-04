from typing import List

class Solution:
    def depthSumRecu(self, nestedList: List[NestedInteger], depth) -> int:
        curSum = 0
        for item in nestedList:
            if not item.isInteger():
                curSum += self.depthSumRecu(item.getList(), depth + 1)
            else:
                curSum += depth * item.getInteger()
            
        return curSum

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.depthSumRecu(nestedList, 1)
