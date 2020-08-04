from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        withFirst = self.robSimple(nums[0:-1])
        skipFirst = self.robSimple(nums[1:])

        return max(withFirst, skipFirst)

    def robSimple(self, nums: List[int]) -> int:
        oneBack = 0
        twoBack = 0
        for cur in nums:
            temp = oneBack
            oneBack = max(twoBack + cur, oneBack)
            twoBack = temp
        return oneBack
        


n = [2,3,2]
s = Solution()
res = s.rob(n)
print(res)
# print(n[1:])