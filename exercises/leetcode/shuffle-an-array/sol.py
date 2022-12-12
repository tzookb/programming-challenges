from typing import List, Counter
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        arr = self.original.copy()
        for i in range(self.size):
            replace_idx = random.randint(0, self.size - 1)
            arr[i], arr[replace_idx] = arr[replace_idx], arr[i]
        
        return arr



# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
param_1 = obj.reset()
print(obj.shuffle())
