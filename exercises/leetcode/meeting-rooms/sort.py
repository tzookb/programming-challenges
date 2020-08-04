from typing import List
import collections
from functools import cmp_to_key

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        def owncomp(a, b):
            return 1 if a[0] > b[0] else -1

        rs = sorted(intervals, key=cmp_to_key(owncomp))
        rs.insert(0, [0,0])
        for i in range(1, len(rs)):
            prevEnd = rs[i-1][1]
            curStart = rs[i][0]
            if curStart < prevEnd:
                return False
        return True

s = Solution()
res = s.canAttendMeetings([[7,10],[2,4]])
print(res)