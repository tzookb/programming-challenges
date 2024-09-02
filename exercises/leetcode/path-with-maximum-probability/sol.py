from typing import List


from typing import Counter, List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    final.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return final


nums = [-1,0,1,2,-1,-4]
s = Solution()

res = s.threeSum(nums)
# res = s.twoSum(nums, 0)
print(res)
