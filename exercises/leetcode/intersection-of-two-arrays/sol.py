from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first = {}
        for v in nums1:
            first[v] = True
        final = {}
        for v in nums2:
            if v in first:
                final[v] = True
        return final.keys()