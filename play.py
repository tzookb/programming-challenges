from typing import Counter, List, Optional

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_left = [1]
        from_right = [1]

        for i in range(len(nums)):
            inverse = len(nums) - 1 - i
            left = nums[i]
            right = nums[inverse]
            from_left.append(from_left[-1] * left)
            from_right.insert(0, from_right[0] * right)

        result = []
        for i in range(len(nums)):
            result.append(
                from_left[i] * from_right[i+1]
            )
        return result


s = Solution()
res = s.productExceptSelf([-1,1,0,-3,3])
print(res)
