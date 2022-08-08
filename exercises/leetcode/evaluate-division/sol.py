from typing import Counter, List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        final = []
        connections = self.getConnections(equations, values)
        for query in queries:
            top, bottom = query
            if top == bottom:
                if top in connections:
                    final.append(1)
                else:
                    final.append(-1)
                
                continue
            res = self.findVal(top, bottom, connections)
            final.append(res)
        return final

    def findVal(self, dividee, divider, connections):
        queue = [[dividee, 1]]
        visited = {}
        while queue:
            cur, mult = queue.pop(0)
            if cur in visited:
                continue
            visited[cur] = True
            if cur == divider:
                return mult
            neighbours = []
            if cur not in connections:
                continue
            for conn in connections[cur]:
                con_mult = connections[cur][conn]
                queue.append([conn, mult * con_mult])
        return -1


    def getConnections(self, equations: List[List[str]], values: List[float]):
        connections = {}
        for i in range(len(equations)):
            left, right = equations[i]
            val = values[i]
            if left not in connections:
                connections[left] = {}
            if right not in connections:
                connections[right] = {}
            
            connections[left][right] = val
            connections[right][left] = 1/val
        return connections

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]


s = Solution()
res = s.calcEquation(equations, values, queries)
print(res)