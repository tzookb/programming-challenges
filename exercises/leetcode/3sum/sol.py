from typing import List


class Solution:
    def twoSum(self, nums: List[int], target) -> List[List[int]]:
        nums.sort()
        start = 0
        end = len(nums) - 1
        pairs = []

        while start < end:
            sVal = nums[start]
            eVal = nums[end]
            curSum = sVal + eVal
            if curSum == target:
                pairs.append([sVal, eVal])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
            elif curSum < target:
                start += 1
            elif curSum > target:
                end -= 1

        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = []
        nums.sort()
        prevNum = None
        for idx in range(len(nums) - 1):
            num = nums[idx]
            if num > 0:
                break
            if num == prevNum:
                continue
            prevNum = num
            pairs = self.twoSum(nums[idx+1:], 0 - num)
            for pair in pairs:
                sols.append([num] + pair)

        return sols



nums = [-1,0,1,2,-1,-4]
s = Solution()

res = s.threeSum(nums)
# res = s.twoSum(nums, 0)
print(res)
