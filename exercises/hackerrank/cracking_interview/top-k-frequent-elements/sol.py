from collections import Counter

class Solution:
    def popMax(self, countdDict) -> int:
        theMaxKey = None
        theMaxVal = float("-inf")
        for key in countdDict:
            v = countdDict[key]
            if v > theMaxVal:
                theMaxVal = v
                theMaxKey = key
        del countdDict[theMaxKey]
        return theMaxKey
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()
        for num in nums:
            c[num] += 1
        
        result = []
        for i in range(k):
            curMax = self.popMax(c)
            result.append(curMax)
        
        return result
        
        
        