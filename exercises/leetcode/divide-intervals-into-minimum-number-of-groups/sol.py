from heapq import heappop, heappush
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        groups_ends = [float("inf")]
        for interval in intervals:
            if interval[0] > groups_ends[0]:
                heappop(groups_ends)
            heappush(groups_ends, interval[1])

        return len(groups_ends) - 1


intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
s = Solution()
res = s.minGroups(intervals)
print(res)
