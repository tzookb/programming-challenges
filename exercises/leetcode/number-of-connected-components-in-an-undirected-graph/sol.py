from typing import List, Optional

# I was lazy here, just relied on this solution:
# exercises/leetcode/number-of-provinces/sol.py

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        for src, dest in edges:
            mat[src][dest] = 1
            mat[dest][src] = 1
        return self.findCircleNum(mat)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        circles = 0

        not_visited = {}
        for num in range(len(isConnected)):
            not_visited[num] = True
        
        print(not_visited)
        while not_visited:
            next_val = next(iter(not_visited))
            bfs = [next_val]
            circles += 1
            while bfs:
                cur = bfs.pop(0)
                if cur not in not_visited:
                    continue
                del not_visited[cur]
                for idx, ngb in enumerate(isConnected[cur]):
                    if ngb == 0:
                        continue
                    bfs.append(idx)
        return circles

s = Solution()
print(
    s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]),
    3
)
print(
    s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]),
    2
)
