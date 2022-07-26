from typing import Counter, List, Optional

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queued = []

        for idx, num in enumerate(nums):
            while queued and queued[-1][1] <= num:
                queued.pop()
            
            while queued and (idx - queued[0][0]) >= k:
                queued.pop(0)

            queued.append((idx, num))

            if idx + 1 < k:
                continue
            if len(queued) > 1:
                res.append(queued[0][1])
            else:
                res.append(num)

        return res


nums = [10,1,1,1,1,1,1]
k = 3

s = Solution()
res = s.maxSlidingWindow(nums, k)
print(res)
