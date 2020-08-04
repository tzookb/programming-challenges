from typing import List
import math

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            middle = start + math.floor((end - start) / 2)
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                end = middle-1
            else:
                start = middle+1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        foundIdx = self.binarySearch(nums, target)
        if foundIdx == -1:
            return [-1, -1]

        endIdx = foundIdx
        while endIdx + 1 < len(nums):
            if nums[endIdx + 1] != target:
                break
            endIdx += 1

        startIdx = foundIdx
        while startIdx - 1 >= 0:
            if nums[startIdx - 1] != target:
                break
            startIdx -= 1
        
        return [startIdx, endIdx]

s = Solution()
# res = s.searchRange([5,7,7,8,8,10], 10)
res = s.searchRange([1,1,2], 1)
# res = s.binarySearch([5,7,7,8,8,10], 8)
print(res)