from typing import List
import collections

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        meetings = collections.Counter()
        maxV = float('-inf')

        for iv in intervals:
            meetings[iv[0]] += 1
            meetings[iv[1]] -= 1
            maxV = max(maxV, iv[0], iv[1])
        
        
        mt = [0] * (maxV + 1)
        for meeting in meetings:
            mt[meeting] = meetings[meeting]

        i = 1
        while i < maxV + 1:
            mt[i] = mt[i] + mt[i-1]
            i += 1
        
        for x in mt:
            if x > 1:
                return False
        return True

s = Solution()
res = s.canAttendMeetings([[7,10],[2,4]])
print(res)