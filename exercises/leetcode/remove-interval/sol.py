from typing import List, Dict, Tuple
# https://www.youtube.com/watch?v=zx5Sw9130L0
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        sol = []

        for item in intervals:
            if item[0] >= toBeRemoved[1]:
                sol.append(item)
                continue
            if item[1] <= toBeRemoved[0]:
                sol.append(item)
                continue
            if item[0] >= toBeRemoved[0] and item[1] <= toBeRemoved[1]:
                continue
            
            if item[0] < toBeRemoved[0]:
                sol.append([item[0], toBeRemoved[0]])
            if item[1] > toBeRemoved[1]:
                sol.append([toBeRemoved[1], item[1]])

        return sol


intervals = [[0,2],[3,4],[5,7]]
toBeRemoved = [1,6]
s = Solution()
res = s.removeInterval(intervals, toBeRemoved)
print(res)