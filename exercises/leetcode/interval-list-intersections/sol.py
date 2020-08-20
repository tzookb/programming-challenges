from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0
        merged = []

        while a < len(A) and b < len(B):
            low = max(A[a][0], B[b][0])
            hi = min(A[a][1], B[b][1])
            if low <= hi:
                merged.append([low, hi])

            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1

        return merged
        
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
sol = Solution()
res = sol.intervalIntersection(A, B)
print(res)
