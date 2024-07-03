from functools import cmp_to_key
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        removed_cnt = 0
        prev_end = -1
        
        def compare(item1, item2):
            if item1[0] == item2[0]:
                return item2[1] - item1[1]
            return item1[0] - item2[0]
        
        intervals = sorted(intervals, key=cmp_to_key(compare))

        for itvl in intervals:
            if itvl[1] <= prev_end:
                removed_cnt += 1
            else:
                prev_end = itvl[1]
        
        return len(intervals) - removed_cnt
