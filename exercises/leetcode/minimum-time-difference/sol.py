# import math

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minsFrom00 = [int(tp[:2]) * 60 + int(tp[3:]) for tp in timePoints]
        minsFrom00.sort()
        minsFrom00.append(1440 + minsFrom00[0])

        minVal = float("inf")
        
        for i in range(len(minsFrom00) - 1):
            prev = minsFrom00[i]
            cur = minsFrom00[i + 1]
            minVal = min(minVal, abs(cur - prev))

        return minVal
