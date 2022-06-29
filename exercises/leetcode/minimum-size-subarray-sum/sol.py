from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:        
        left = 0
        cur_sum = 0
        min_subarr_len = float("inf")

        for i in range(len(nums)):
            from_right = nums[i]
            cur_sum += from_right
            while cur_sum >= target:
                cur_len = i - left + 1
                min_subarr_len = min(min_subarr_len, cur_len)
                cur_sum -= nums[left]
                left += 1

        return min_subarr_len if min_subarr_len != float("inf") else 0


target = 7
nums = [5]

s = Solution()
res = s.minSubArrayLen(target, nums)
print(res)