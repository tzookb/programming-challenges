from typing import Counter, List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.getGraph(prerequisites)
        res = self.isCyclic(graph)
        return not res

    def isCyclic(self, graph) -> bool:
        visited = {}
        nest = {}

        def dfs(node):
            if node in visited:
                return False
            if node not in graph:
                return False

            visited[node] = True
            nest[node] = True
            
            for child in graph[node]:
                if child in nest:
                    return True
                
                if dfs(child):
                    return True
            
            del nest[node]
        
        for node in graph:
            if node in visited:
                continue
            if dfs(node):
                return True

        return False


    def getGraph(self, prerequisites: List[List[int]]):
        connections = {}
        for dependee, dependor in prerequisites:
            if dependor not in connections:
                connections[dependor] = {}
            connections[dependor][dependee] = True
        return connections


numCourses = 2
prerequisites = [[1,0]]
# prerequisites = [[1,0],[0,1]]

s = Solution()
res = s.canFinish(numCourses, prerequisites)
print(res)