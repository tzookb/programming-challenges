from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        if not intervals:
            return merged
        intervals.sort(key=lambda x: x[0])
        curStart = intervals[0][0]
        curEnd = intervals[0][1]
        for x in intervals:
            if curEnd >= x[0]:
                curEnd = max(x[1], curEnd)
            else:
                merged.append([curStart, curEnd])
                curStart = x[0]
                curEnd = x[1]

        merged.append([curStart, curEnd])
        return merged