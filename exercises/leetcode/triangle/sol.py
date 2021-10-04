from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row_idx in range(1, len(triangle)):
            prev_row = triangle[row_idx - 1]
            for col_idx in range(len(triangle[row_idx])):
                options = []
                if col_idx == 0 or col_idx == len(triangle[row_idx]) - 1:
                    if col_idx == 0:
                        options.append(prev_row[0])
                    if col_idx == len(triangle[row_idx]) - 1:
                        options.append(prev_row[-1])
                else:
                    options.append(prev_row[col_idx])
                    options.append(prev_row[col_idx - 1])
                triangle[row_idx][col_idx] += min(options)
        return min(triangle[-1])

s = Solution()
tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = s.minimumTotal(tri)
print(res)
