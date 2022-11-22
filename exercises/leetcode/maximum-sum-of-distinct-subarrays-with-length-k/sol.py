from typing import Counter, Dict, List, Optional

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = Counter()
        cur_sum = 0
        max_sum = cur_sum
        left = right = 0

        def isvalid():
            print(counts, len(counts) == k)
            return len(counts) == k
        def isWindowSizeValid():
            # print(right, left, right - left + 1 == k)
            return right - left + 1 == k

        while right < len(nums):
            right_val_add = nums[right]
            counts[right_val_add] += 1
            cur_sum += right_val_add

            if not isWindowSizeValid():
                right += 1
                continue
            
            if isvalid():
                max_sum = max(max_sum, cur_sum)

            left_val_remove = nums[left]
            counts[left_val_remove] -= 1
            if counts[left_val_remove] == 0:
                del counts[left_val_remove]
            cur_sum -= left_val_remove
            left += 1
            right += 1

        return max_sum


s = Solution()
sol = s.maximumSubarraySum([1,5,4,2,9,9,9], 3)
# sol = s.maximumSubarraySum([4,4,4], 3)
# sol = s.maximumSubarraySum([1,1,1,7,8,9], 3)
print(sol)