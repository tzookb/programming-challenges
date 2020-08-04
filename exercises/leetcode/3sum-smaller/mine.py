from typing import List

class Solution:
    def getAllPairs(self, numbers: List[int]) -> List[List[int]]:
        results = []
        for i, a in enumerate(numbers):
            for b in numbers[i+1:]:
                results.append([a,b])
        return results

    def twoSumSmaller(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        results = []
        while start < end:
            startV = numbers[start]
            endV = numbers[end]
            total = startV + endV

            if total >= target:
                end -= 1
            else:
                results.append([startV, endV])
                start += 1

        return results

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        results = []
        for i in range(len(nums)):
            a = nums[i]
            leftArr = nums[i+1:]
            pairs = self.twoSumSmaller(leftArr, target - a)
            for pair in pairs:
                results.append([a] + pair)
        return results
            

nums = [-2,0,1,3]
target = 2
s = Solution()
res = s.threeSumSmaller(nums, target)
# res = s.twoSumSmaller(nums, target)
# res = s.getAllPairs(nums)
print(res)
