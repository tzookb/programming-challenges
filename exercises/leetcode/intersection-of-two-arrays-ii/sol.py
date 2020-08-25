from typing import List
import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first = collections.Counter()
        for v in nums1:
            first[v] += 1
        final = collections.Counter()
        for v in nums2:
            if v in first and first[v] > 0:
                first[v] -= 1
                final[v] += 1

        finalArr = []
        for val in final:
            count = final[val]
            for i in range(count):
                finalArr.append(val)
        return finalArr

s = Solution()
res = s.intersection(
    [1,1,1,2],
    [1,1,]
)
print(res)