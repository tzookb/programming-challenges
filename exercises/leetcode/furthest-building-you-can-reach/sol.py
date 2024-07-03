from typing import List, Counter
from heapq import heappush, heappop, heapify

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diffs = [0]
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            diff = max(0, diff)
            diffs.append(diff)
        
        top_climbs = []
        bricks_needed = 0
        postion = -1
        for climb in diffs:
            postion += 1
            if len(top_climbs) < ladders:
                heappush(top_climbs, climb)
                continue
            if top_climbs and top_climbs[0] < climb:
                to_add = heappop(top_climbs)
                heappush(top_climbs, climb)
                bricks_needed += to_add
            else:
                bricks_needed += climb

            if bricks_needed > bricks:
                postion -= 1
                break

        return postion



s = Solution()
# res = s.furthestBuilding(heights=[4,2,7,6,9,14,12], bricks=5, ladders=1) #4
# res = s.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2) # 7
res = s.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0) # 3
print(res)