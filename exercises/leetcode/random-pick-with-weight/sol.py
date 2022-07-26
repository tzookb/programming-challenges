import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.presums = []
        self.total_sum = 0

        for weight in w:
            self.total_sum += weight
            self.presums.append(self.total_sum)
        

    def pickIndex(self) -> int:
        rand_val = random.randrange(0, self.total_sum)
        
        for idx, cur_step in enumerate(self.presums):
            if rand_val < cur_step:
                return idx
