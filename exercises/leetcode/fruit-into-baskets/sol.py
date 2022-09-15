from typing import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter()
        left = right = total = 0
        
        while right < len(fruits):
            cur = fruits[right]
            count[cur] += 1
            while len(count) > 2:
                cur = fruits[left]
                left += 1
                count[cur] -= 1
                if count[cur] == 0:
                    del count[cur]
            
            total = max(total, right - left + 1)
            right += 1
        
        return total
                