from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromLeft = [nums[0]]
        fromRight = [nums[-1]]

        for i in range(len(nums)-1):
            startI = i + 1
            reverseI = len(nums) - 1 - startI

            curLeftVal = nums[startI]
            curRightVal = nums[reverseI]

            prevStart = fromLeft[-1]
            prevEnd = fromRight[0]

            fromLeft.append(curLeftVal * prevStart)
            fromRight.insert(0, curRightVal * prevEnd)

        solArr = []

        for i in range(len(nums)):
            if i == 0:
                solArr.append(fromRight[1])
                continue
            if i == len(nums) - 1:
                solArr.append(fromLeft[-2])
                continue
            solArr.append(fromLeft[i-1] * fromRight[i+1])

        return solArr

n = [1, 2, 3, 4]
s = Solution()
res = s.productExceptSelf(n)
print(res)