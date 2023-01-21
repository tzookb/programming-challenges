from typing import List, Optional
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [{0: 1}]
        for num in nums:
            prev_sums = dp[-1]
            next_sums = {}
            for prevsum in prev_sums:
                val = prev_sums[prevsum]
                

                
                added = prevsum + num
                subtr = prevsum - num
                if added not in next_sums:
                    next_sums[added] = 0
                if subtr not in next_sums:
                    next_sums[subtr] = 0

                next_sums[added] += val
                next_sums[subtr] += val
            
            dp.append(next_sums)

        if target not in next_sums:
            return 0

        return next_sums[target]

s = Solution()
s.findTargetSumWays([1,1,1,1,1], 3)
