from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copied = arr.copy()
        unique_list = (list(set(copied)))
        unique_list.sort()

        ranks = {}
        for idx, x in enumerate(unique_list):
            ranks[x] = idx + 1

        result = []

        for item in arr:
            result.append(ranks[item])

        return result

s = Solution()
res = s.arrayRankTransform([40,10,20,30,10])
print(res)