from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result = []
        stack = []

        for height in heights[::-1]:
            count = 0
            while stack and stack[-1] < height:
                count += 1
                stack.pop()
            if stack:
                count += 1

            stack.append(height)
            result.append(count)

        return result[::-1]



heights = [10,6,8,5,11,9]
# Output: [3,1,2,1,1,0]
s = Solution()
res = s.canSeePersonsCount(heights)
print(res)