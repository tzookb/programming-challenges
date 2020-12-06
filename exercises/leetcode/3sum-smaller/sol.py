from typing import List

class Solution:

    def twoSumSmaller(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        count = 0
        while start < end:
            total = numbers[start] + numbers[end]
            if total < target:
                count += end - start 
                start += 1
            else:
                end -= 1
        return count

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()
        for i in range(len(nums)-2):
            a = nums[i]
            leftArr = nums[i+1:]
            curTarget = target - a
            curCount = self.twoSumSmaller(leftArr, curTarget)
            result += curCount
        return result


nums = [3,1,0,-2]
target = 4
s = Solution()
res = s.threeSumSmaller(nums, target)
# res = s.twoSumSmaller([0,1,3], 4)
# res = s.getAllPairs(nums)
print(res)
