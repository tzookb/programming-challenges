from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        addition_rules = [[0 for _ in range(n)] for _ in range(n)]
        final = [[0 for _ in range(n)] for _ in range(n)]

        for query in queries:
            for row in range(query[0], query[2] + 1):
                query[1], query[3]
                addition_rules[row][query[1]] += 1
                if query[3] + 1 < n:
                    addition_rules[row][query[3] + 1] -= 1

        for row in range(n):
            cur = 0
            for col in range(n):
                cur += addition_rules[row][col]
                final[row][col] = cur

        return final

n = 3
queries = [[1,1,2,2],[0,0,1,1]]
s = Solution()
res = s.rangeAddQueries(n, queries)
print(res)
