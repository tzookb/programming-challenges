from typing import List
from heapq import heappush, heappop


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        paths = self._getPaths(edges, succProb)
        visited = {}
        heap = [(-1, start_node)]
        max_prob = 0

        while heap:
            neg_prob, cur_node = heappop(heap)
            cur_prob = -neg_prob  # Convert back to positive probability
            
            if cur_node in visited and visited[cur_node] >= cur_prob:
                continue
            
            visited[cur_node] = cur_prob
            
            if cur_node == end_node:
                max_prob = max(max_prob, cur_prob)
                continue 

            if cur_node not in paths:
                continue
            
            for neighbor in paths[cur_node]:
                edge_prob = paths[cur_node][neighbor]
                new_prob = cur_prob * edge_prob
                heappush(heap, (-new_prob, neighbor))
        
        return max_prob


    def _getPaths(self, edges: List[List[int]], succProb: List[float]) -> dict[int, float]:
        paths = {}
        for edge, prob in zip(edges, succProb):
            e1, e2 = edge
            if e1 not in paths:
                paths[e1] = {}
            if e2 not in paths:
                paths[e2] = {}
            
            paths[e1][e2] = prob
            paths[e2][e1] = prob
        
        return paths

s = Solution()
# n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2

# 0.3
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.3]
start = 0
end = 2

# 0
n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2

# xxxx
n = 5
edges = [[2,3],[1,2],[3,4],[1,3],[1,4],[0,1],[2,4],[0,4],[0,2]]
succProb = [0.06,0.26,0.49,0.25,0.2,0.64,0.23,0.21,0.77]
start = 0
end = 3

n = 500
edges = [[193,229],[133,212],[224,465]]
succProb = [0.91,0.78,0.64]
start = 4
end = 364

res = s.maxProbability(n, edges, succProb, start, end)
print(res)