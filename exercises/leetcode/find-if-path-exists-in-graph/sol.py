from typing import Counter, List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        paths = self.getPathsMap(edges)

        if source not in paths:
            return False
        
        visited = {}
        queue = [source]
        while queue:
            cur = queue.pop(0)
            if cur in visited:
                continue
            visited[cur] = True
            if cur == destination:
                return True
            if cur not in paths:
                continue
            
            for path in paths[cur]:
                queue.append(path)

        return False

    def getPathsMap(self, edges: List[List[int]]) -> dict:
        paths = {}
        for edge in edges:
            fromnode, tonode = edge
            if fromnode not in paths:
                paths[fromnode] = {}
            paths[fromnode][tonode] = True
            if tonode not in paths:
                paths[tonode] = {}
            paths[tonode][fromnode] = True
            
        return paths

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

s = Solution()
res = s.validPath(n, edges, source, destination)
print(res)