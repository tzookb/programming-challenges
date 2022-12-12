from typing import List, Counter
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque(maxlen=size)
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.queue.maxlen:
            self.sum -= self.queue.popleft()
        self.sum += val
        self.queue.append(val)
        
        return self.sum / len(self.queue)

