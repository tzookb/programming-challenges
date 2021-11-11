from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] + k

        leftCount = k
        for i in range(1, len(nums)):
            cur = nums[i]
            prev = nums[i - 1]
            diff = cur - prev - 1
            if leftCount <= diff:
                return prev + leftCount
            leftCount -= diff

        return nums[-1] + leftCount


s = Solution()
res = s.missingElement([4,7,9,10], 3)
print(res)

print(s.missingElement([4,7,9,10], 1) == 5)
print(s.missingElement([4], 1) == 5)
print(s.missingElement([0,4], 2) == 2)
print(s.missingElement([0,4], 4) == 5)
print(s.missingElement([0,4], 4) == 5)
print(s.missingElement([1,2,4], 3) == 6)