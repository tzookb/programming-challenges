class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        connected = 0
        
        while left < right:
            connected += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        
        if left == right:
            connected += int(nums[left])

        return connected
