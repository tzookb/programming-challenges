from typing import List

class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True

        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                increasing = False
            if A[i-1] < A[i]:
                decreasing = False

        return increasing or decreasing

s = Solution()
res = s.isMonotonic([1,3,2])
print(res)