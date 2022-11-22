class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}
        
        cur = n
        while cur != 1:
            summed = 0
            temp_cur = cur
            while temp_cur:
                digit = temp_cur % 10
                summed += digit**2
                temp_cur = temp_cur // 10

            if summed in visited:
                return False
            visited[summed] = True
            cur = summed
        
        return True
