from typing import List
from collections import deque 

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mappings = {}
        stack = deque()
        
        for num in nums2:
            if not stack:
                stack.append(num)
                continue
            if stack[-1] > num:
                stack.append(num)
                continue
            while stack and stack[-1] < num:
                item = stack.pop()
                mappings[item] = num
            stack.append(num)

        while stack:
            item = stack.pop()
            mappings[item] = -1

        return list(map(lambda x: mappings[x], nums1))

nums1 = [4,1,2]
nums2 = [1,2,3,4,5]
s = Solution()
res = s.nextGreaterElement(nums1, nums2)
print(res)