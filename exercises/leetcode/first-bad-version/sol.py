# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        lastBad = float("inf")
        
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                lastBad = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return lastBad