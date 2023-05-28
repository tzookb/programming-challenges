from typing import List, Optional

class Solution:
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

