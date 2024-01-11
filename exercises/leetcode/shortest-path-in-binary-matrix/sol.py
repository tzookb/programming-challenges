from typing import List, Optional

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        cur = (0, 0)
        rows = len(grid)
        cols = len(grid[0])
        end = (rows - 1, cols - 1)
        visited = {}

        is_passable = lambda pos: grid[pos[0]][pos[1]] == 0
        is_out = lambda pos: pos[0] < 0 or pos[0] >= rows or pos[1] < 0 or pos[1] >= cols

        bfs = [(cur, 1)]

        while bfs:
            
            step, length = bfs.pop(0)
            # print(step)
            # print(bfs)
            # print('------')
            if step in visited:
                continue
            if is_out(step):
                continue
            visited[step] = True
            if not is_passable(step):
                continue

            if step == end:
                return length
            
            bfs.append(((step[0] - 1, step[1] - 1), length + 1))
            bfs.append(((step[0] - 1, step[1] + 1), length + 1))
            bfs.append(((step[0] - 1, step[1]), length + 1))

            bfs.append(((step[0], step[1] - 1), length + 1))
            bfs.append(((step[0], step[1] + 1), length + 1))

            bfs.append(((step[0] + 1, step[1] - 1), length + 1))
            bfs.append(((step[0] + 1, step[1]), length + 1))
            bfs.append(((step[0] + 1, step[1] + 1), length + 1))

        return -1





s = Solution()
res = s.shortestPathBinaryMatrix([
    [0,0,0],
    [1,1,0],
    [1,1,0]
])
print(res)