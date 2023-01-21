class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
            cur = num
            while cur:
                digit = cur % 10
                total -= digit
                cur = cur // 10
        return total