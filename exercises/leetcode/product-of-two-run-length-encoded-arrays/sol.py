from typing import List, Counter, Optional
from heapq import heappush, heappop, heapify

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        idx1 = 0
        idx2 = 0
        sol = [[None, 0]]

        while idx1 < len(encoded1) and idx2 < len(encoded2):
            val1, cnt1 = encoded1[idx1]
            val2, cnt2 = encoded2[idx2]

            mincount = min(cnt1, cnt2)

            encoded1[idx1][1] -= mincount
            encoded2[idx2][1] -= mincount

            mult = val1 * val2

            if sol[-1][0] == mult:
                sol[-1][1] += mincount
            else:
                sol.append([mult, mincount])

            if encoded1[idx1][1] == 0:
                idx1 += 1

            if encoded2[idx2][1] == 0:
                idx2 += 1
        
        return sol[1:]



s = Solution()
res = s.findRLEArray(
    [[3,5],[2,1]],
    [[3,3],[2,2],[3,1]]
)

print(res)
