class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        matches = {}
        for i, n in enumerate(nums):
            if n not in matches:
                matches[n] = i
                continue
            
            if i - matches[n] <= k:
                return True

            matches[n] = i

        return False
        