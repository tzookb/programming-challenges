from typing import Counter, List, Optional
import heapq

class Node(object):
    def __init__(self, dist: int, val: int):
        self.dist = dist
        self.val = val

    def __lt__(self, other):
        if self.dist == other.dist:
            return self.val < other.val

        return self.dist < other.dist

def printNodes(arr):
    print(list(map(lambda x: x.val, arr)))

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for item in arr:
            dist = abs(x - item)
            heapq.heappush(heap, Node(dist, item))
        
        result = []
        for _ in range(k):
            cur_node = heapq.heappop(heap)
            result.append(cur_node.val)
        
        result.sort()
        return result

# arr = [1,2,3,4,5]
# k = 4
# x = 3

arr = [1,2,5,5,6,6,7,7,8,9]
k = 7
x = 7

s = Solution()
res = s.findClosestElements(arr, k, x)
print(res)