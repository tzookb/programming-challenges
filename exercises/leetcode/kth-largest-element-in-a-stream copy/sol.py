from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        with_new_interval = self.insertSingle(intervals, newInterval)
        return self.merge(with_new_interval)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        already_merged = False
        merged_intervals = [intervals[0]]
        for idx in range(1, len(intervals)):
            cur = intervals[idx]
            prev = merged_intervals[-1]
            if cur[0] <= prev[1]:
                merged_intervals[-1][1] = max(cur[1], merged_intervals[-1][1])
                already_merged = True
                continue

            if already_merged:
                merged_intervals += intervals[idx:]
                return merged_intervals
            else:
                merged_intervals.append(cur)

        return merged_intervals

    def insertSingle(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for idx, interval in enumerate(intervals):
            if newInterval[0] <= interval[0]:
                intervals = intervals[0:idx] + [newInterval] + intervals[idx:]
                return intervals
        return intervals + [newInterval]
# Input: 


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# Output: [[1,5],[6,9]]
s = Solution()
res = s.insert(intervals, newInterval)
print(res)