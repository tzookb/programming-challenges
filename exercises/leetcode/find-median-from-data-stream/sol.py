from typing import List, Counter
from heapq import heappush, heappop, heapify

class MinHeap:
    def __init__(self):
        self.items = []
    def add(self, num):
        heappush(self.items, num)
    def pop(self):
        return heappop(self.items)
    def empty(self):
        return bool(self.items)
    def readTop(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def print(self):
        return self.items
class MaxHeap(MinHeap):
    def add(self, num):
        super().add(-num)
    def pop(self):
        return -super().pop()
    def readTop(self):
        return -super().readTop()
    def print(self):
        return [-item for item in self.items]

class MedianFinder:

    def __init__(self):
        self.smalls = MaxHeap()
        self.bigs = MinHeap()

    def addNum(self, num: int) -> None:
        if self.smalls.size() > self.bigs.size():
            if self.smalls.readTop() > num:
                biggest_small = self.smalls.pop()
                self.smalls.add(num)
                self.bigs.add(biggest_small)
            else:
                self.bigs.add(num)
        elif self.smalls.size() < self.bigs.size():
            if self.bigs.readTop() < num:
                smallest_big = self.bigs.pop()
                
                self.smalls.add(smallest_big)
                self.bigs.add(num)
            else:
                self.smalls.add(num)
        else:
            if self.bigs.size() and self.bigs.readTop() < num:
                self.bigs.add(num)
            else:
                self.smalls.add(num)

    def findMedian(self) -> float:
        if self.smalls.size() == self.bigs.size():
            return (self.smalls.readTop() + self.bigs.readTop()) / 2

        if self.smalls.size() > self.bigs.size():
            return self.smalls.readTop()

        return self.bigs.readTop()


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
obj.addNum(10)
obj.addNum(1)
obj.addNum(1)
obj.addNum(5)
obj.addNum(3)
medi = obj.findMedian()
print("smalls:", obj.smalls.print())
print("bigs:", obj.bigs.print())
print("medi:", medi)
