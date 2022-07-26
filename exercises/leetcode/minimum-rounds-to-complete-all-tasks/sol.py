from typing import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        rounds = 0 
        for diff in cnt:
            amount = cnt[diff]
            while amount > 4:
                rounds += 1
                amount -= 3
            if amount == 4:
                rounds += 2
            elif amount == 3:
                rounds += 1
            elif amount == 2:
                rounds += 1
            elif amount == 1:
                return -1

        return rounds        
                
        