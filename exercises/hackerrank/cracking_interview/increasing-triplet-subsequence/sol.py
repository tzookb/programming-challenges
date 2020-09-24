class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        sec = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= sec:
                sec = num
            else:
                return True
        return False
        