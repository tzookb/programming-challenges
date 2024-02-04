from typing import List, Dict, Tuple
# https://www.youtube.com/watch?v=zx5Sw9130L0
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxed = 0
        stack = []

        for i, height in enumerate(heights):
            while stack and stack[-1][X] < height:

heights = [2,1,5,6,2,3]
s = Solution()
res = s.largestRectangleArea(heights)
print(res)