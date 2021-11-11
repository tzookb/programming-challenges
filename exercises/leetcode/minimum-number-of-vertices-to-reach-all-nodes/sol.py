from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_edge_count = [0] * n
        
        for edge in edges:
            source = edge[0]
            dest = edge[1]
            in_edge_count[dest] += 1
        
        starts = []
        for item_idx, val in enumerate(in_edge_count):
            if val == 0:
                starts.append(item_idx)
        
        return starts

k = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
s = Solution()
res = s.findSmallestSetOfVertices(k, edges)
print(res)