class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        cur = num
        while cur:
            dig = cur % 10
            if num % dig == 0:
                count += 1
            cur = cur // 10
        
        return count