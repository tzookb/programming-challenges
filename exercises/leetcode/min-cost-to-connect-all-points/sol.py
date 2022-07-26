from typing import Counter, List, Optional
import heapq

class Point:
    def __init__(self, idx, dist):
        # print(idx, dist)
        self.idx = idx
        self.dist = dist

    def __lt__(self, nxt):
        return self.dist < nxt.dist

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        closest = []
        visited = {}
        heapq.heapify(closest)
        heapq.heappush(closest, Point(0, 0))
        cost = 0

        while closest and len(visited.keys()) < len(points):
            cur = heapq.heappop(closest)
            if cur.idx in visited:
                continue
            visited[cur.idx] = True
            main_point = points[cur.idx]
            cost += cur.dist

            # print(cur.idx, cur.dist)
            for idx in range(len(points)):
                if idx == cur.idx:
                    continue
                cur_point = points[idx]
                dist = (
                    abs(main_point[0] - cur_point[0]) + 
                    abs(main_point[1] - cur_point[1])
                )
                heapq.heappush(closest, Point(idx, dist))

        return cost

points = [[3,12],[-2,5],[-4,1]]
# points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
s = Solution()
res = s.minCostConnectPoints(points)
print(res)
