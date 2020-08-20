from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        moveToNext = 0
        countedZeros = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[moveToNext] = nums[idx]
                moveToNext += 1
            else:
                countedZeros += 1

        for i in range(countedZeros):
            nums[-(i+1)] = 0
        
s = Solution()
arr = [0,1,0,3,12]
res = s.moveZeroes(arr)
print(arr)
