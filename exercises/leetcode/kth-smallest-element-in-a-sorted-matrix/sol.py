from typing import List, Counter
from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        first = (matrix[0][0], 0, 0)
        heap = [first]
        count = 1

        visited = {}
        while count < k:
            cur, row, col = heappop(heap)
            if row + 1 < rows and (row + 1, col) not in visited:
                visited[(row + 1, col)] = True
                heappush(heap, (matrix[row + 1][col], row + 1, col))
            if col + 1 < cols and (row, col + 1) not in visited:
                visited[(row, col + 1)] = True
                heappush(heap, (matrix[row][col + 1], row, col + 1))
            
            count += 1
        return heap[0][0]
        

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
matrix = [
    [1,3,5],
    [6,7,12],
    [11,14,14]
]
k = 6
s = Solution()
res = s.kthSmallest(matrix, k)
print(res)