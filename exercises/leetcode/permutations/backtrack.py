from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def recu(cur, nums):
            # print(nums, cur)
            if cur == len(nums):
                sol.append(nums[:])
                return

            for i in range(cur, len(nums)):
                nums[cur], nums[i] = nums[i], nums[cur]
                recu(cur + 1, nums)
                nums[cur], nums[i] = nums[i], nums[cur]

        recu(0, nums)

        return sol

s = Solution()
res = s.permute([1,2,3])
print(res)