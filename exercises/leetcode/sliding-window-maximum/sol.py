from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        total = len(nums)
        rounds = total - k + 1
        curRound = 0
        curMax = float('-inf')
        maxes = []

        while curRound < rounds:
            window = nums[curRound:curRound+k]
            if curRound == 0:
                curMax = max(window)
            else:
                removed = nums[curRound - 1]
                added = nums[curRound + k - 1]
                if added > curMax:
                    curMax = added
                elif removed == curMax:
                    curMax = max(window)
                else:
                    pass

            maxes.append(curMax)
            curRound += 1

        return maxes

s = Solution()
res = s.maxSlidingWindow(
    [1,3,-1,-3,5,3,6,7], 3
    # [1,3,-1,-3, 2], 3
)
print(res)