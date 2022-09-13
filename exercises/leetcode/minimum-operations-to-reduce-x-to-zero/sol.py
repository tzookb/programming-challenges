from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        orig_len = len(nums)
        target = sum(nums) - x
        cur = 0
        left = 0
        right = 0
        min_size = float("inf")
        while right < len(nums):
            rightval = nums[right]
            cur += rightval
            if cur == target:
                min_size = min(min_size, orig_len - (right - left + 1))
            while cur > target and left <= right:
                leftval = nums[left]
                cur -= leftval
                left += 1
            if cur == target:
                min_size = min(min_size, orig_len - (right - left + 1))
            right += 1
        return min_size if min_size != float("inf") else -1

nums = [1,1,4,2,3]
x = 5
# nums = [5,6,7,8,9]
# x = 4
# nums = [3,2,20,1,1,3]
# x = 10


s = Solution()
res = s.minOperations(nums, x)
print(res)