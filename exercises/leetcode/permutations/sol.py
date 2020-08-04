from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permuteRecu(nums)

    def permuteRecu(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [[nums[0]]]

        fullpermuts = []

        for i in range(len(nums)):
            dig = nums[i]
            leftNums = nums[0:i] + nums[i+1:]
            permuts = self.permuteRecu(leftNums)
            for permut in permuts:
                fullpermuts.append([dig] + permut)

        return fullpermuts