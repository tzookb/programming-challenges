from typing import List, Counter
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_points = 2
        for i in range(len(points)):
            cnts = Counter()
            for j in range(len(points)):
                if i == j:
                    continue
                angle = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
                print(angle)
                cnts[angle] += 1
            
            cur_max = max(cnts.values()) + 1
            max_points = max(max_points, cur_max)

        return max_points


# points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# points = [[4,5],[4,-1],[4,0]]
# points = [[-6,-1],[3,1],[12,3]] # 3
points = [[1,1],[2,2],[3,3]]
s = Solution()
res = s.maxPoints(points)
print(res)
