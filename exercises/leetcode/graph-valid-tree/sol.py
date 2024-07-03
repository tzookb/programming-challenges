from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pointers = [{} for _ in range(n)]
        
        for edge in edges:
            pointers[edge[0]][edge[1]] = True
            pointers[edge[1]][edge[0]] = True
        
        bfs = [0]
        seen = {}

        while bfs:
            cur = bfs.pop(0)
            if cur in seen:
                return False
            seen[cur] = True

            for neighb in pointers[cur]:
                bfs.append(neighb)
                del pointers[neighb][cur]
        
        return n == len(seen)

s = Solution()
# res = s.validTree(5, [[0,1],[0,2],[0,3],[1,4]]) # 1
# res = s.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]) # 0
# res = s.validTree(2, [[1, 0]]) # 1
res = s.validTree(3, [[1, 0], [2, 0]]) # 1
print(res)