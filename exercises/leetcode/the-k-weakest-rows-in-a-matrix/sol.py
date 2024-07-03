from typing import List, Counter
from heapq import heappush, heappop

class Row: 
    def __init__(self, idx, soldiers): 
        self.idx = idx 
        self.soldiers = soldiers

    def __lt__(self, nxt): 
        if self.soldiers == nxt.soldiers:
            return self.idx < nxt.idx
        return self.soldiers < nxt.soldiers


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for idx in range(len(mat)):
            line = mat[idx]
            soldiers = sum(line)
            row = Row(idx, soldiers)
            heappush(heap, row)

        sol = []
        for _ in range(k):
            cur = heappop(heap)
            sol.append(cur.idx)

        return sol

mat = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
]
k = 3

s = Solution()
res = s.kWeakestRows(mat, k)
print(res)