from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)

        curMin = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            for j in range(i):
                comp = nums[j]

                if cur > comp:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

s = Solution()
# res = s.lengthOfLIS([10, 9, 2, 5, 3, 4])
res = s.lengthOfLIS([1,2,3,4,5,6,7,5,3,7,101,3])
print(res)