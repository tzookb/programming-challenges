from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        leftidx = 0
        the_max =  float("-inf")
        
        for i in range(1, len(values)):
            left = values[leftidx]
            right = values[i]
            cur = left + right + leftidx - i

            the_max = max(the_max, cur)
            
            if left + leftidx < right + i:
                leftidx = i

        return the_max

s = Solution()
res = s.maxScoreSightseeingPair([8,1,5,2,6])
print(res)