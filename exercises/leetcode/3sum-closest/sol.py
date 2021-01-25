from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float("inf")
        final_sum = 0
        for idx, num in enumerate(nums):
            start = idx + 1
            end = len(nums) - 1
            cur_target = target - num
            while start < end:
                cur_sum = nums[start] + nums[end]
                cur_diff = abs(cur_target - cur_sum)
                if cur_diff < min_diff:
                    min_diff = cur_diff
                    final_sum = num + nums[start] + nums[end]
                if cur_sum > cur_target:
                    end -= 1
                else:
                    start += 1
        return final_sum


s = Solution()
res = s.threeSumClosest([-1,2,1,-4], target = 1)
# -4, -1, 1, 2
print(res)