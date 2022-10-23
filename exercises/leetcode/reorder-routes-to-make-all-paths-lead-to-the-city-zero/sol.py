from typing import Counter, Dict, List, Optional

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirectedgraph = self.createUndirectedGraph(connections)
        directedgraph = self.createDirectedGraph(connections)
        reorders = 0
        visited = {}
        
        dfs = [0]
        while dfs:
            cur = dfs.pop()
            if cur in visited:
                continue
            if cur not in undirectedgraph:
                continue

            visited[cur] = True

            neighbours = undirectedgraph[cur]
            for neighbour in neighbours:
                dfs.append(neighbour)
                if neighbour in visited:
                    continue
                if cur not in directedgraph:
                    continue
                if neighbour not in directedgraph[cur]:
                    continue
                print(cur, neighbour)
                reorders += 1
            # print(cur)
            # print(dfs)

        return reorders


    def createUndirectedGraph(self, connections: List[List[int]]) -> Dict:
        graph = {}
        for con in connections:
            fromnode, tonode = con
            if fromnode not in graph:
                graph[fromnode] = {}
            graph[fromnode][tonode] = True
            if tonode not in graph:
                graph[tonode] = {}
            graph[tonode][fromnode] = True
        return graph

    def createDirectedGraph(self, connections: List[List[int]]) -> Dict:
        graph = {}
        for con in connections:
            fromnode, tonode = con
            if fromnode not in graph:
                graph[fromnode] = {}
            graph[fromnode][tonode] = True
        return graph

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
s = Solution()
res = s.minReorder(n, connections)
print(res)