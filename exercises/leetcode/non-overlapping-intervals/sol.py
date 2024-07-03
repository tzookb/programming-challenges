from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        skipped = 0
        prev = 0

        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] < intervals[prev][1]:
                skipped += 1
                continue
            else:
                prev = i
        
        return skipped

s = Solution()
# res = s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
res = s.eraseOverlapIntervals([[1,2],[1,2],[1,2]])
print(res)