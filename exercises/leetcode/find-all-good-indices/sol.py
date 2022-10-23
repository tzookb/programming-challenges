from typing import Counter, List, Optional

class Solution:
    def getItems(self, nums: List[int], k: int) -> List[int]:
        res = [False] * len(nums)
        count = 0
        prev = float("inf")
        for i in range(len(nums)):
            if count >= k:
                res[i] = True

            cur = nums[i]
            if cur > prev:
                count = 1
                prev = cur
                continue
            count += 1
            
            prev = cur
        return res

    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        left = [False] * len(nums)
        right = [False] * len(nums)

        left = self.getItems(nums, k)
        right = self.getItems(nums[::-1], k)[::-1]


        final = []
        for idx, (a, b)  in enumerate(zip(left, right)):
            if a == b == True:
                final.append(idx)

        return final




s = Solution()
res = s.goodIndices([2,1,1,1,3,4,1], 2)
# res = s.goodIndices([2,1,1,2], 2)
# res = s.goodIndices([2,1,2], 1)
# res = s.goodIndices([1,2,1,2], 1)
print(res)