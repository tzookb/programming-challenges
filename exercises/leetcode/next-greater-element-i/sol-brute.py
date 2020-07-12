from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = []
        idx = 0
        while idx < len(nums1):
            num1 = nums1[idx]
            found = False
            secIdx = nums2.index(num1) + 1
            while secIdx < len(nums2):
                num2 = nums2[secIdx]
                secIdx += 1
                if num2 > num1:
                    nextGreater.append(num2)
                    found = True
                    break
            idx += 1
            if not found:
                nextGreater.append(-1)
        return nextGreater



nums1 = [4,1,2]
nums2 = [1,3,4,2]
s = Solution()
res = s.nextGreaterElement(nums1, nums2)
print(res)