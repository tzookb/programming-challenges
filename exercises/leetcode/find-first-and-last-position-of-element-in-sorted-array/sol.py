from typing import List

class Solution:
    def binarySearch(self, nums: List[int], target: int, pushTo) -> List[int]:
        start = 0
        end = len(nums) - 1
        foundItem = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                foundItem = mid
                if pushTo == "left":
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return foundItem

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftFound = self.binarySearch(nums, target, "left")
        if leftFound == -1:
            return [-1, -1]
        rightFound = self.binarySearch(nums, target, "right")
        
        return [leftFound, rightFound]

s = Solution()
res = s.searchRange([5,7,7,8,8,8,8,8,8,10], 8)
print(res)