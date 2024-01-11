from typing import List, Dict, Tuple
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights)):
            cur = heights[i]
            while stack and heights[stack[-1]] <= cur:
                stack.pop()
            stack.append(i)
        
        return stack

s = Solution()
res = s.findBuildings([4,2,3,1])

print(res)

