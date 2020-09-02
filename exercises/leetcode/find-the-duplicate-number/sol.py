from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            num = nums[i]
            sum += i + 1
            sum -= num
        print(sum)
        

s = Solution()
res = s.findDuplicate([1,3,4,2,2])
print(res)