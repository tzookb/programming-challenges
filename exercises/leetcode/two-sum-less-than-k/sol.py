from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return -1
        nums.sort()
        left = 0
        right = len(nums) - 1
        max_sum = -1
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum < k:
                left += 1
                max_sum = max(max_sum, cur_sum)
            else:
                right -= 1
        
        return max_sum

nums = [34,23,1,24,75,33,54,8]
k = 60
nums = [10,20,30]
k = 15

s = Solution()
res = s.twoSumLessThanK(nums, k)
print(res)
