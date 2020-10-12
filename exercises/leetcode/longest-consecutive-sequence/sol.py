from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        maxStreak = 0
        
        for num in setnums:
            if num - 1 not in setnums:
                cur = num
                streak = 0
                while cur in setnums:
                    streak += 1
                    cur += 1
                maxStreak = max(maxStreak, streak)
        return maxStreak

s = Solution()
res = s.longestConsecutive([1,2,3,4,1,1,2])
print(res)