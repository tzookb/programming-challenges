from typing import List
from collections import defaultdict, deque, Counter

class Solution:
    def getMaxFromMatrix(self, mat: List[List[int]]) -> int:
        return_max = float("-inf")
        for row in mat:
            return_max = max(return_max, max(row))
        return return_max

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [([0] * (len(nums1) + 1)) for x in range(len(nums2) + 1)]

        for i in range(len(nums2)):
            for j in range(len(nums1)):
                dpi = i + 1
                dpj = j + 1
                if nums2[i] == nums1[j]:
                    dp[dpi][dpj] = dp[dpi - 1][dpj - 1] + 1
        return self.getMaxFromMatrix(dp)

s = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

res = s.findLength(nums1, nums2)
print(res)