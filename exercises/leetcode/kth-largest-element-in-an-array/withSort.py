from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort(reverse=True)
        print(nums)
        for num in nums:
            count += 1
            if count == k:
                return num
        return -1

s = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
res = s.findKthLargest(nums, k)
print(res)