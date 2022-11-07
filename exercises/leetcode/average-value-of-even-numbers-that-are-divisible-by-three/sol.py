class Solution:
    def averageValue(self, nums: List[int]) -> int:
        counted = 0
        total = 0
        for num in nums:
            if num % 3 or num % 2:
                continue
            counted += 1
            total += num
        
        if not counted:
            return 0
            
        return total // counted