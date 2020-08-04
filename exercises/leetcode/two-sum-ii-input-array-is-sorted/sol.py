from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            startV = numbers[start]
            endV = numbers[end]
            total = startV + endV

            if total == target:
                return [start+1, end+1]

            if total > target:
                end -= 1
            else:
                start += 1
            
        return []