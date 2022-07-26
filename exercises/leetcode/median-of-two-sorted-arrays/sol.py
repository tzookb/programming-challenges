from typing import List
import math

class Solution:
    def popItem(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 and nums2:
            if nums1[0] < nums2[0]:
                return nums1.pop(0)
            else:
                return nums2.pop(0)
        if nums1:
            return nums1.pop(0)
        if nums2:
            return nums2.pop(0)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1+nums2)
        prelength = math.floor(length / 2)
        poppedCnt = 0
        popped = []
        while poppedCnt <= prelength:
            popped.append(self.popItem(nums1, nums2))
            poppedCnt += 1
        
        if length % 2 == 0:
            return (popped[-1] + popped[-2]) / 2
        else:
            return popped[-1]

s = Solution()
res = s.findMedianSortedArrays(
    [1, 3, 6, 7],
    [2, 4, 5]
)
print(res)