from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - len(nums2) - 1
        j = len(nums2) - 1
        end = len(nums1) - 1
        
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[end] = nums2[j]
                j -= 1
            else:
                nums1[end] = nums1[i]
                i -= 1
            end -= 1

        while j >= 0:
            nums1[end] = nums2[j]
            j -= 1
            end -= 1

s = Solution()
a = [4,5,6,0,0,0]
s.merge(
    a,
    3,
    [1,2,3],
    3
)
print(a)