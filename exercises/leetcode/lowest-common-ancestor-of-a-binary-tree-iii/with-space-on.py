from typing import List, Counter, Optional
from heapq import heappush, heappop, heapify

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = {}
        rn = p
        while rn:
            visited[rn] = True
            rn = rn.parent
        
        rn = q
        while rn:
            if rn in visited:
                return rn
            rn = rn.parent
