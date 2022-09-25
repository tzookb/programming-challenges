from typing import Counter, List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        graph, not_pointed_to = self.getGraph(matrix)
        memo = {}
        def dfs(node):
            if node in memo:
                return memo[node]
            if node not in graph:
                memo[node] = 1
                return 1
            connections = graph[node]

            max_dist = 0
            for con in connections:
                max_dist = max(max_dist, dfs(con))
            
            memo[node] = max_dist + 1
            return max_dist + 1

        longest = 0
        for cur in not_pointed_to:
            cur_dist = dfs(cur)
            longest = max(longest, cur_dist)
        
        return longest

    def getGraph(self, matrix: List[List[int]]) -> int:
        graph = {}
        pointed_to = Counter()

        def getKey(row, col):
            return f"{row}_{col}"
        def addNext(row, col, nextrow, nextcol):
            key = getKey(row, col)
            if key not in graph:
                graph[key] = {}
            if nextrow < 0 or nextrow >= len(matrix):
                return
            if nextcol < 0 or nextcol >= len(matrix[0]):
                return
            cur_val = matrix[row][col]
            next_val = matrix[nextrow][nextcol]

            if cur_val >= next_val:
                return

            next_key = getKey(nextrow, nextcol)
            pointed_to[next_key] -= 1
            
            graph[key][next_key] = True

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                cur_key = getKey(row, col)
                pointed_to[cur_key] += 1
                addNext(row, col, row - 1, col)
                addNext(row, col, row + 1, col)
                addNext(row, col, row, col - 1)
                addNext(row, col, row, col + 1)

        not_pointed = []
        for key in pointed_to:
            if pointed_to[key] == 1:
                not_pointed.append(key)
        return [graph, not_pointed]

# matrix = [[9,9,4],[6,6,8],[2,1,1]]
# matrix = [[3,4,5],[3,2,6],[2,2,1]]
# matrix = [[1]]
matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
s = Solution()
res = s.longestIncreasingPath(matrix)
print(res)