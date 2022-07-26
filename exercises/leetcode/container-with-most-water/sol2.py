from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            left_val = height[left]
            right_val = height[right]
            width = right - left
            cur_area = min(left_val, right_val) * width
            max_area = max(max_area, cur_area)

            if left_val > right_val:
                right -= 1
            else:
                left += 1
        
        return max_area


arr = [1,8,6,2,5,4,8,3,7]
arr = [1,1]
s = Solution()
res = s.maxArea(arr)
print(res)