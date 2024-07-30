from typing import List, Counter, Optional
from heapq import heappush, heappop, heapify

class EncodedArrCreator:
    def __init__(self) -> None:
        self.coded = []
        self.prev = None
        self.count = 0

    def add(self, val) -> None:
        if val == self.prev:
            self.count += 1
            return
        
        if self.prev == None:
            self.prev = val
            self.count = 1
            return
        
        self.coded.append([self.prev, self.count])
        self.prev = val
        self.count = 1
    
    def get(self) ->  List[List[int]]:
        return self.coded + [[self.prev, self.count]]

class EncodedArr:
    def __init__(self, coded: List[List[int]]) -> None:
        self.coded = coded
        self.outer_idx = 0
        self.inner_idx = 0
    
    def pop(self) -> int:
        if self.outer_idx >= len(self.coded):
            return None
        group = self.coded[self.outer_idx]
        num, count = group
        if self.inner_idx + 1 > count:
            self.outer_idx += 1
            self.inner_idx = 0
            return self.pop()
        
        self.inner_idx += 1
        return num


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        exp1 = EncodedArr(encoded1)
        exp2 = EncodedArr(encoded2)
        
        multed = EncodedArrCreator()
        while True:
            v1 = exp1.pop()
            v2 = exp2.pop()
            if v1 is None:
                break
            val = v1 * v2

            multed.add(val)
        
        return multed.get()


s = Solution()
res = s.findRLEArray(
    [[2,3]],
    [[3,3]]
)
# res = s.expand([[1,2],[3,4],[5,6]])
# res = s.collapse([1, 1, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5])
# res = s.collapse([1])
print(res)
# er = EncodedArr([[1,1], [3,4], [5, 2]])
# print(er.pop())
# print(er.pop())
# print(er.pop())
# print(er.pop())
# print(er.pop())
# print(er.pop())
# print(er.pop())

